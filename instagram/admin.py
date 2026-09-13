from django.contrib import admin
from .models import Instagram

@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ['link', 'order', 'is_active']
