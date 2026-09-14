from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Service


@receiver([post_save, post_delete], sender=Service)
def clear_home_cache(sender, **kwargs):
    cache.clear()