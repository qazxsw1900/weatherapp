from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def log_out(request):
    logout(request)
    response = redirect('/')
    return response

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(username=username, password=password, email=email)
        if user is not None:
            messages.error(request, 'User already exists')
            return render(request, 'account/register.html')
        else:
            try:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                return redirect('/account/login')
            except:
                messages.error(request, 'User already exists')
    return render(request, 'account/register.html')

def log_in(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/')
            return response
        else:
            messages.error(request, 'Incorrect Password or Username')
    return render(request, 'account/login.html')