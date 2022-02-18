from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null

# Create your models here.

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64)
    iLevel = models.IntegerField(null=False)
    guildRole = models.CharField(max_length=64, default="Member")
    classe = models.CharField(max_length=64, default="")
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"Owner: {self.user} Name:{self.name} iLevel:{self.iLevel} Class: {self.classe} Guild: {self.guild}"

   
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

# class Content(models.Model):
#     contentName = models.CharField(max_length=64) # ContentName (ex: PvP, GvG, Raid 4man, raid 8 man)
    
#     def __str__(self):
#         return f"Content Name:{self.contentName}"

# class Group(models.Model):
#     groupName = models.CharField(max_length=64)
#     charName = models.ForeignKey(Character, on_delete=models.CASCADE)
#     content = models.ForeignKey(Content, on_delete=models.CASCADE, default="")
#     def __str__(self):
#         return f"Group Name:{self.groupName} Name:{self.charName}"