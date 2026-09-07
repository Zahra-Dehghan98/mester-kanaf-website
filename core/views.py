from django.shortcuts import render
from django.views.generic import TemplateView
from services.models import Service

class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active = True).order_by("order")
        return context
    

