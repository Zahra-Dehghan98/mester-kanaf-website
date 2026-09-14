from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Portfolio, PortfolioImage


@receiver([post_save, post_delete], sender=Portfolio)
def clear_home_cache(sender, **kwargs):
    cache.clear()

@receiver([post_save, post_delete], sender=PortfolioImage)
def clear_home_cache(sender, **kwargs):
    cache.clear()