from django.views.generic import TemplateView
from services.models import Service
from products.models import Product
from portfolio.models import Portfolio
from testimonials.models import Testimonial
from instagram.models import Instagram
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60 * 60 * 24 * 365), name="dispatch")
class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active = True).order_by("order")
        context["products"] = Product.objects.filter(is_active = True).order_by("order")
        context["portfolios"] = Portfolio.objects.filter(is_active = True).order_by("-created_at")[:6]
        context["testimonials"] = Testimonial.objects.filter(is_approved = True).order_by("-created_at")
        context["instagram_posts"] = Instagram.objects.filter(is_active = True).order_by("order")
        return context