from django.views import View
from django.http import JsonResponse
from .models import Contact


class ContactView(View):
    def post(self, request):
        errors = []
        
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
    
        if len(name) < 3:
            errors.append("طول نام نباید کمتر از ۳ کاراکتر باشد")
        if len(phone) < 11:
            errors.append("شماره تماس باید ۱۱ رقم باشد")
        if len(message) < 10:
            errors.append("طول پیام نباید کمتر از ۱۰ کاراکتر باشد")
        if len(message) > 500:
            errors.append("طول پیام نباید بیشتر از ۵۰۰ کاراکتر باشد")
        
        if errors:
            return JsonResponse({"status": "error", "errors": errors})
        
        Contact.objects.create(
            name=name,
            phone=phone,
            subject=subject,
            message=message
        )
        return JsonResponse({"status": "success"})