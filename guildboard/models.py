from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass

class Classe(models.Model): 
    className = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.className}"

class Guild(models.Model):
    guildName = models.CharField(max_length=64)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.guildName}"  

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    iLevel = models.IntegerField()
    guildRole = models.CharField(max_length=64, default="")
    className = models.ForeignKey(Classe, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return f"Owner: {self.user} Name:{self.name} iLevel:{self.iLevel} Class: {self.className} Guild: {self.guild}"

   
class Content(models.Model):
    contentName = models.CharField(max_length=64) # ContentName (ex: PvP, GvG, Raid 4man, raid 8 man)
    
    def __str__(self):
        return f"Content Name:{self.contentName}"

class Group(models.Model):
    groupName = models.CharField(max_length=64)
    charName = models.ForeignKey(Character, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, default="")
    def __str__(self):
        return f"Group Name:{self.groupName} Name:{self.charName}"