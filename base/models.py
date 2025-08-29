from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50,null=True,blank=True)
    email  = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    
    avatar  = models.ImageField(null=True,default='avatar.svg',upload_to='')
    
   # yfdfgsSDTGGSCV@#$%5454
   
    REQUIRED_FIELDS = []
    

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Room (models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='rooms')
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    description = models.TextField(null=True , blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on','-updated_on']
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on','-updated_on']
        
    def __str__(self):
        return self.body[0:30]