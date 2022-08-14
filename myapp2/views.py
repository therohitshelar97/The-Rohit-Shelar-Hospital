from operator import is_
from django.shortcuts import render, HttpResponseRedirect
from .models import Appointment
#from CRUDE.myapp2.models import Appointment
from .forms import Appointmentform, SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created succesfully')
            fm.save()
            fm = SignUpForm()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html',{'form':fm})

#login view 
def Page_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile/')
    return render(request, 'login.html', {'form':fm})

def profile(request):
    if request.user.is_authenticated:
        fm = EditUserProfileForm(instance=request.user)
        return render(request, 'profile.html', {'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')
#logou page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def facilities(request):
    return render (request, 'facilities.html')

def medicines(request):
    if request.user.is_authenticated:
        return render(request, 'medicines.html')
    else:
        return HttpResponseRedirect('/login/')

def appointment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm44 = Appointmentform(request.POST)
            if fm44.is_valid():
                fm44.save()
                return HttpResponseRedirect('/login/')
        else:
            fm44 = Appointmentform()
        appoint = Appointment.objects.all()
        return render (request, 'appointment.html', {'fm44':fm44, 'appoint':appoint})

#Chang
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render (request, 'change_pass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')