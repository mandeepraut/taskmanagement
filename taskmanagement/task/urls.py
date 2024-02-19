from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name=''),
    path('create-task/',views.createTask,name='create-task'),
    path('view-tasks/',views.viewTasks,name='view-tasks'),
    path('update-task/<str:pk>/',views.updateTask,name='update-task'),
    path('delete-task/<str:pk>/',views.deleteTask,name='delete-task'),
    path('register/',views.register,name="register"),
    path('my_login/',views.my_login,name="my-login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('profile-management/',views.profile_management,name="profile-management"),
    path('delete-account/',views.deleteAccount,name="delete-account"),
    path('user-logout/',views.user_logout,name="user-logout"),
    


]
