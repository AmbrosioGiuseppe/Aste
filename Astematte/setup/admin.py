from django.contrib import admin
from setup.models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomeMenu', 'slugUrl', 'url', 'attivo',)
    #list_filter, da decidere che filtri utilizzare
    #list_editable, da decidere che campi saranno possibili editare

admin.site.register(Menu, MenuAdmin)