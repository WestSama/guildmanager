from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import CreateUserForm

def index(request):
    return render(request, "guildboard/addcharacter.html")

def loginView(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect("index")
        else:
            messages.info(request, "Username OR Password is incorrect")

    context = {}
    return render(request, "guildboard/login.html", context)

def registerView(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            
            return redirect('login')

    context = {"form":form}
    return render(request, "guildboard/register.html", context)

def logoutView(request):
    logout(request)
    return redirect("login")

def addCharacter(request):
    pass