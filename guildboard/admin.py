from django.contrib import admin
from .models import *
# Register your models here.

class GuildsAdmin(admin.ModelAdmin):
    list_display = ['guildName', 'capacity']
    

class CharacterAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'className', 'iLevel', 'guild', 'guildRole']

admin.site.register(User)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Classe)
admin.site.register(Guild, GuildsAdmin)
admin.site.register(Group)
admin.site.register(Content)