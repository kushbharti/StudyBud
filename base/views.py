from django.shortcuts import render


# Create your views here.

rooms =[
   {'id':1,'name':"hello"},
   {'id':2,'name':'hii'},
   {'id':3,'name':'guys'}
]

my_dict={
   'name':'kush',
   'age':19,
   'class':'S.E-IT'
}

def home(request):
   return render(request,'home.html',{'rooms':rooms,'dict':my_dict})

def index(request,pk):
   room = None
   for i in rooms:
      if i['id'] == int(pk):
         room =i
         
   return render(request,'index.html',{'rooms':room})