from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import Room,User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1','password2']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']
        

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['name','email','bio','avatar']