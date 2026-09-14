from django.apps import AppConfig


class TestimonialsConfig(AppConfig):
    name = 'testimonials'

    def ready(self):
        import testimonials.signals 
