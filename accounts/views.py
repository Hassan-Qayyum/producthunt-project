from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']

        if request.POST['password'] == request.POST['confirmpassword']:
            user = User.objects.filter(username = username)
            if not user:
                user = User.objects.create_user(username= request.POST['username'], password= request.POST['password'])
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request,'accounts/signup.html',{'usernameError':'Username already exists'})
        else:
            return render(request,'accounts/signup.html',{'passwordError':'Password & confirm password must be same !'})

    return render (request,'accounts/signup.html')

def login(request):

    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password= request.POST['password'])
        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Invalid Credentials'})
    return render(request,'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
