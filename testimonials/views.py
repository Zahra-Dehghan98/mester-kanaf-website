from django.views.generic import FormView
from .forms import TestimonialForm
from .models import Testimonial
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect

class TestimonialView(FormView):
    form_class = TestimonialForm
    template_name = "core/index.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        errors = []
        name = form.cleaned_data.get("name")
        if len(name) < 3:
            errors.append("طول نام نباید کمتر از 3 کاراکتر باشد")
        message = form.cleaned_data.get("message")
        if len(message) < 10 :
            errors.append("طول پیام نباید کمتر از 10 کاراکتر باشد")
        if len(message) > 500 :
            errors.append("طول پیام نباید بیشتر از 500 کاراکتر باشد")
        if Testimonial.objects.filter(message=message).exists():
            errors.append("این نطر قبلا ثبت شده است")
        if errors:
            return JsonResponse({"status": "error", "errors": errors})
        form.save()
        return JsonResponse({"status": "success"})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.filter(is_approved=True).order_by("-created_at")
        return context
        

        
