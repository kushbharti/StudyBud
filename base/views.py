from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms =[
#    {'id':1,'name':"hello"},
#    {'id':2,'name':'hii'},
#    {'id':3,'name':'guys'}
# ]

# my_dict={
#    'name':'kush',
#    'age':19,
#    'class':'S.E-IT'
# }

def home(request):
   rooms = Room.objects.all()
   return render(request,'base/home.html',{'rooms':rooms})

def index(request,pk):
   room = Room.objects.get(id=pk)
   return render(request,'base/index.html',{'rooms':room})