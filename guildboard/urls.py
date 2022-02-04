from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("logout/", views.logoutView, name="logout"),

    path("addcharacter/", views.addCharacter, name="addCharacter"),
    path("updatechar/<str:pk>/", views.updateChar, name="updatechar"),
    path("deletechar/<str:pk>/", views.deleteChar, name="deletechar"),

    path("wizzels/", views.wizzelsPage, name="wizzels"),
]
