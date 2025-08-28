from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    
    path('',views.home,name='home'),
    path('index/<int:pk>/',views.index,name='index'),
    path('user-profile/<int:pk>/',views.userProfile,name='user-profile'),
    
    path('create-room/',views.create_room,name='create-room'),
    path('update-room/<int:pk>/',views.update_room,name='update-room'),
    path('delete-room/<int:pk>/',views.delete_room,name='delete-room'),
    
    path('delete-msg/<int:pk>/',views.deleteMsg,name='delete-msg'),
    path('update-user/',views.updateUser,name='update-user')
]