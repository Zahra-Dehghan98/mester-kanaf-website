from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Portfolio, PortfolioImage

class PortfolioImageInline(TabularInline):
    model = PortfolioImage
    extra = 3 
    fields = ['image', 'order']
    
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'order', 'is_active']
    inlines = [PortfolioImageInline]