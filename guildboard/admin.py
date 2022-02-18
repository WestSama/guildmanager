from django.contrib import admin
from .models import *
# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "iLevel", "classe", "guild", "guildRole",]
    list_filter = ('guild', 'guildRole', "classe")
    search_fields = ["name"]

    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Character, CharacterAdmin)
admin.site.register(Guild)
admin.site.register(Group)
admin.site.register(Content)
admin.site.register(Classe)
admin.site.register(Image)