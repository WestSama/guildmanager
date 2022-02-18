from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import os

from guildboard.models import Character, Classe, Image

from .forms import CreateUserForm, CharacterForm, ImageForm

@login_required(login_url='/login/')
def index(request):
    user = request.user
    context = {
        "chars":Character.objects.filter(user=user)
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
    else :
        form = UserCreationForm()
        context = {"form":form}
        return render(request, "guildboard/register.html", context)   
            
    context = {"form":form}
    return render(request, "guildboard/register.html", context)

def logoutView(request):
    logout(request)
    return redirect("login")

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def updateChar(request, pk):
    
    char = Character.objects.get(id=pk)
    form = CharacterForm(instance=char)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=char)
        if form.is_valid():
            form.save()
            messages.success(request, "Character has been updated!")
            return redirect('index')

    context = {"form":form}
    return render(request, "guildboard/updatechar.html", context)

@login_required(login_url='/login/')
def deleteChar(request, pk):
    
    char = Character.objects.get(id=pk)
    char.delete()

    return redirect("index")

@login_required(login_url='/login/')
def guildPage(request):
    chars = Character.objects.all()
    context = {"chars":chars}
    return render(request, "guildboard/guild.html", context)

@login_required(login_url='/login/')
def gallery(request):
    images = Image.objects.all().order_by('-id')

    imagePaginator = Paginator(images, 10)
    page_num = request.GET.get('page')
    page = imagePaginator.get_page(page_num)

    context = {
        "images":images,
        "page": page
    }
    return render(request, "guildboard/gallery.html", context)

@login_required(login_url='/login/')
def viewImage(request, pk):
    image = Image.objects.get(pk=pk)
    context = {
        "image":image
    }
    return render(request, "guildboard/viewimage.html", context)

@login_required(login_url='/login/')
def addImage(request):
    
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        print("image:", image)

        imageData = Image.objects.create(
            user=request.user,
            description=data["description"],
            image=image
        )
        imageData.save()  
        return redirect('gallery')
    context = {
        
    }
    return render(request, "guildboard/addimage.html", context)

@login_required(login_url='/login/')
def deleteImage(request, pk):
    image = Image.objects.get(pk=pk)
    if len(image.image) > 0:
        os.remove(image.image.path)
    image.delete()
    return redirect("gallery")