from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
admin.register(MyUser)
# Register your models here.

class MyUserAdmin(UserAdmin):
    pass