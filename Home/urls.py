from django.contrib import admin
from django.urls import path, include
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('register/', include('Register.urls'), name='register'),
    path('dashboard/', include('Dashboard.urls'), name='dashboard'),
    path('profile/', include('Profile_info.urls'), name='ProfileInfo'),
    path('login/', views.handleSLogin, name='login'),
    path('logout/', views.handleSLogout, name='logout'),
    path('loadLive/', views.loadLive, name='loadLive'),
    path('testLoadCache/', views.testLoadCache, name='testLoadCache'),
    path('testWriteCache/', views.testWriteCache, name='testWriteCache'),


]
