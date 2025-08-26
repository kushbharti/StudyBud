from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Room, Topic,Message
from .forms import RoomForm
from django.http import HttpResponse
from django.db.models import Q ,Count

# Create your views here.


def loginPage(request):
   
   page = 'login'   
   if request.user.is_authenticated:
      return redirect('home')
  
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      try:
         user = User.objects.get(username= username)
      except:
         messages.error(request,'User does not Exist')
         
      user = authenticate(request,username=username,password=password)
      
      if user is not None:
         login(request,user)
         return redirect('home')
      else:
         messages.error(request,'Username & Password does not exist')
         
   context ={'page':page}
   return render(request,'base/login_register.html',context)



def logoutUser(request):
   logout(request)
   return redirect('login')



def registerPage(request):
   form = UserCreationForm()
   
   try:
      if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request,user)
           return redirect('home')
        
   except Exception as e :
      print('Error Occurs',e)
   context = {'form':form}
   return render(request,'base/login_register.html',context)



@login_required(login_url='login')
def home(request):   
   try:
      q = request.GET.get('q')  if request.GET.get('q') != None else ""
      
      rooms = Room.objects.filter(Q(topic__name__icontains = q)|
                                  Q(name__icontains = q) |
                                  Q(description__icontains = q))
     
      room_count = rooms.count()
      topics = Topic.objects.annotate(room_count=Count('topic',filter=Q(topic__in=rooms)))
      context = {'rooms':rooms,'topics':topics,'room_count':room_count}
   except Exception as e :
      print('Error',e)
      return HttpResponse(f'something Wrong {e}')
   return render(request,'base/home.html',context)



def index(request,pk):
   try:
      room = Room.objects.get(id=pk)
      room_messages = room.message_set.all().order_by('-created_on')
      participants = room.participants.all()
      if request.method == 'POST':
         message = Message.objects.create(user =request.user,
                                          room = room,
                                          body=request.POST.get('body')
                                          )
         room.participants.add(request.user)
         return redirect('index',pk=room.id)
      
      context = {'room':room,'room_messages':room_messages,'participants':participants}
      return render(request,'base/index.html',context)
   except Exception as e:
      print('Error', e)
      return HttpResponse(f"Something went wrong: {e}")



@login_required(login_url='login')
def create_room(request):
   form = RoomForm()
   try:
      if request.method == 'POST':
         form = RoomForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('home')
      context = {'form':form}
   except Exception as e:
      print('Error', e)
      return HttpResponse("Error Occurs")
   return render(request,'base/create_room.html',context)



@login_required(login_url='login')
def delete_room(request,pk):
   room = Room.objects.get(id=pk)
   try:
     if request.method =='POST':
        room.delete()
        return redirect('home')
   except Exception as e:
      print('Error', e)
      return HttpResponse("Somethinge went wronge")
   
   return render(request,'base/delete_room.html',{'obj':room})



@login_required(login_url='login')
def update_room(request,pk):
   room = Room.objects.get(id=pk)
   form = RoomForm(instance=room)
   
   if request.user != room.host:
      return HttpResponse('Not Allowed')
   try:
      if request.POST =='POST':
         form = RoomForm(request.POST, instance=room)
         if form.is_valid():
            form.save()
            return redirect('home')
      context = {'form':form}
   except Exception as e:
      print('Error', e)
      return HttpResponse("Somethinge went wronge") 

   return render(request,'base/create_room.html',context)



@login_required(login_url='login')
def deleteMsg(request,pk):
   msg = Message.objects.get(id=pk)
   if request.user != msg.user:
      return HttpResponse('U are not applicable for this')
   try:
      if request.method == 'POST':
         msg.delete()
         return redirect('home')
   except Exception as e:
      print('Error', e)
      return HttpResponse("Somethinge went wronge")
   return render(request,'base/delete_room.html',{'obj':msg})
   