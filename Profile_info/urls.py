from django.contrib import admin
from django.urls import path, include
from Profile_info import views

urlpatterns = [
    path('', views.profileView, name='profileView'),
    path('edit/', views.editProfile, name='editProfile'),
    path('edit/changePassword', views.changePassword, name='changePassword'),
]
