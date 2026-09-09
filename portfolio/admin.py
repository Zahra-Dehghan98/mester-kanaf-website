from django.contrib import admin
from .models import Portfolio, PortfolioImage

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'order', 'is_active']

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ['portfolio', 'order']