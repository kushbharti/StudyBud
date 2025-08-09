from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/<int:pk>',views.index,name='index')
]