from django.urls import path
from .views import TestimonialView

urlpatterns = [
    path('testimonial/submit/', TestimonialView.as_view(), name='testimonial_submit')
]