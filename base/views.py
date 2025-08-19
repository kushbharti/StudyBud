from django.shortcuts import render,redirect
from .models import Room, Topic
from .forms import RoomForm
from django.http import HttpResponse
from django.db.models import Q ,Count

# Create your views here.


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
      return render(request,'base/index.html',{'rooms':room})
   except Exception as e:
      print('Error', e)
      return HttpResponse(f"Something went wrong: {e}")

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



def update_room(request,pk):
   room = Room.objects.get(id=pk)
   form = RoomForm(instance=room)
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