from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Login/Register/Logout
    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("logout/", views.logoutView, name="logout"),

    # Character routes
    path("addcharacter/", views.addCharacter, name="addCharacter"),
    path("updatechar/<str:pk>/", views.updateChar, name="updatechar"),
    path("deletechar/<int:pk>/", views.deleteChar, name="deletechar"),

    # Guild route
    path("guild/", views.guildPage, name="guild"),

    # Gallery routes
    path("gallery/", views.gallery, name="gallery"),
    path("image/<str:pk>/", views.viewImage, name="image"),
    path("addimage/", views.addImage, name="addimage"),
    path("deleteimage/<str:pk>/", views.deleteImage, name="deleteimage")
]
