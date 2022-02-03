from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("logout/", views.logoutView, name="logout"),

    path("addcharacter/", views.addCharacter, name="addCharacter"),

]
