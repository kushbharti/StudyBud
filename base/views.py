from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Room, Topic,Message,User
from .forms import RoomForm,UserForm,MyUserCreationForm
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
   form = MyUserCreationForm()
   
   try:
      if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
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
                                  Q(description__icontains = q)
                                  )
     
      room_count = rooms.count()
      topics = Topic.objects.annotate(room_count=Count('rooms',filter=Q(rooms__in=rooms)))
      
      room_msgs = Message.objects.filter(Q(room__topic__name__icontains =q))
      
      context = {'rooms':rooms,'topics':topics,'room_count':room_count,'room_msgs':room_msgs}
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
         message = Message.objects.create(user = request.user,
                                          room = room,
                                          body = request.POST.get('body')
                                          )
         room.participants.add(request.user)
         return redirect('index',pk=room.id)
      
      context = {'room':room,'room_messages':room_messages,'participants':participants}
      return render(request,'base/index.html',context)
   except Exception as e:
      print('Error', e)
      return HttpResponse(f"Something went wrong: {e}")



def userProfile(request,pk):
   user = User.objects.get(id=pk)
   rooms = user.room_set.all()
   room_msgs = user.message_set.all()
   topics = Topic.objects.all()   
   context = {'user':user,'rooms':rooms,'room_msgs':room_msgs,'topics':topics}
   return render(request,'base/profile.html',context)



@login_required(login_url='login')
def create_room(request):
   form = RoomForm()
   topics = Topic.objects.all()
   try:
      if request.method == 'POST':
         topic_name = request.POST.get('topic')
         topic, created_on = Topic.objects.get_or_create(name=topic_name)
         Room.objects.create(
            host=request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
         )
       
         return redirect('home')
      context = {'form':form,'topics':topics}
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
   topic = Topic.objects.all()
   if request.user != room.host:
      return HttpResponse('Not Allowed')
   try:
      if request.POST =='POST':
         topic_name = request.POST.get('topics')
         topic, created = Topic.objects.get_or_create(name=topic_name)
         room.topic = topic
         room.name = request.POST.get('name')
         room.description = request.POST.get('description')
         room.save()
         return redirect('home')
      context = {'form':form,'topics':topic,'room':room}
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


@login_required(login_url='login')
def updateUser(request):
   user = request.user
   form = UserForm(instance=user)
   try:
      if request.method == 'POST':
         form = UserForm(request.POST, request.FILES,instance=user)
         if form.is_valid(): 
           form.save() 
           return redirect('user-profile',pk=user.id)
   except Exception as e:
      print('Error', e)
      return HttpResponse("Somethinge went wronge")
   return render(request,'base/update-user.html',{'form':form})



def topicsPage(request):
   q = request.GET.get('q')  if request.GET.get('q') != None else ""
   
   topics = Topic.objects.filter(Q(name__icontains =q)).annotate(room_count=Count('rooms'))
   return render(request,'base/topics.html',{'topics':topics}) 


def activityPage(request):
   room_msg = Message.objects.all()
   return render(request,'base/activity.html',{'room_msg':room_msg})  
   
   
   
