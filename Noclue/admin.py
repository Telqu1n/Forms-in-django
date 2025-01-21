from django.contrib import admin
from .models import LogIn
# Register your models here.

class adminLogIn(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    

admin.site.register(LogIn, adminLogIn)
