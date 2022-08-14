"""CRUDE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views
from myapp2 import views as roh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addandshow/',views.add_show, name="addandshow"),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/',views.update_data, name="updatedata"),
    path('',views.home, name="home"),
    path('signup/', roh.sign_up, name="signup"),
    path('login/', roh.Page_login, name="login"),
    path('profile/', roh.profile, name="profile"),
    path('logout/', roh.user_logout, name="logout"),
    path('facilities/', roh.facilities, name="facilities"),
    path('medicines/',roh.medicines, name="medicines"),
    path('appointment1/', roh.appointment, name="appointment1"),
    path('pass_change/', roh.change_pass, name="pass_change"),
]
