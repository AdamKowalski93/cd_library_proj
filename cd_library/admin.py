from django.contrib import admin
from cd_library.models.CdDescription import *
from cd_library.models.MusicTypes import *


# Register your models here.
class CdInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'artist', 'date']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['type']


admin.site.register(CD, CdInfoAdmin)
admin.site.register(Types, TypesAdmin)

