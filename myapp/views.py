from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrations
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.

#This function will add new items and show all items
def add_show(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = StudentRegistrations(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']
                reg = User(name=nm, email=em, password=pw)
                fm.save()
                fm = StudentRegistrations()
        
        else:
            fm = StudentRegistrations()
        stud = User.objects.all()  
        return render (request, 'addandshow.html', {'form':fm,'stu':stud})
    else:
        return HttpResponseRedirect('/profile/')

def home(request):
    return render (request, 'home.html')

#This function will update or edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistrations(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/addandshow/')

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)

    return render (request, 'updatestudent.html',{"form":fm})

#This function will delete items
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow/')

