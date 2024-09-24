from django.contrib import admin
from .models import Friendship

@admin.register(Friendship)
class FrienshipAdmin(admin.ModelAdmin):
    pass
    #13:51