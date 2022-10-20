from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ['id', 'username', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('coin',)}),
    )

admin.site.register(MyUser,MyUserAdmin)