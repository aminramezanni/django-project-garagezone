from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You logged in successfuly')
            return redirect('dashboard')
        else:
            messages.error(request, 'username or password in invalid')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    messages.success(request,'Yor account has created')
                    return redirect('dashboard')
                    user.save()
        else:
            messages.error(request,'Password and Confirm password are not Equal')
            return redirect('register')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    auth.logout(request)
    # messages.success(request,'Yor has been logged out')
    return redirect('home')
