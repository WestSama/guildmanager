from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages

from guildboard.models import Character, Classe

from .forms import CreateUserForm, CharacterForm

def index(request):
    context = {
        "chars":Character.objects.all()
    }
    return render(request, "guildboard/index.html", context)

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

    if request.method == "POST":
        name = request.POST["charName"]
        iLvl = request.POST["iLevel"]
        classe = request.POST["class"]
        user = request.user
        
        if Character.objects.filter(name=name).exists():
            messages.error(request, "This character already exist.")
            return redirect(reverse("addCharacter"))
        else:
            character = Character.objects.create(
                name = name,
                iLevel = iLvl,
                classe = classe,
                user = user
            )
            character.save()
            messages.success(request, "Your character has been added successfully!")
            return redirect(reverse("addCharacter"))

    context = {"classes" : Classe.objects.all()}    
    return render(request, "guildboard/addcharacter.html", context)   

def updateChar(request, pk):
    
    char = Character.objects.get(id=pk)
    form = CharacterForm(instance=char)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=char)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {"form":form}
    return render(request, "guildboard/updatechar.html", context)

def deleteChar(request, pk):
    
    char = Character.objects.get(id=pk)
    char.delete()

    return redirect("index")

def wizzelsPage(request):
    chars = Character.objects.all()
    context = {"chars":chars}
    return render(request, "guildboard/wizzels.html", context)