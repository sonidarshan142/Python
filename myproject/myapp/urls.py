"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path("logoutuser/",views.logoutuser,name="logoutuser"),
    path("profile",views.profile,name="profile"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("change-profile-password",views.change_profile_password,name="change-profile-password"),
    path("update-profile",views.update_profile,name="update-profile"),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('update-password', views.update_password, name='update-password'),
    path('add-notice', views.add_notice, name='add-notice'),
    path('view-notice', views.view_notice, name='view-notice'),
    path('delete-notice/<int:pk>', views.delete_notice, name='delete-notice'),
    path('edit-notice/<int:pk>', views.edit_notice, name='edit-notice'),
    path('update-notice', views.update_notice, name='update-notice'),
    
]