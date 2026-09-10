from django.views.generic import ListView
from .models import Portfolio

class PortfolioListView(ListView):
    model = Portfolio
    template_name =  "portfolio/portfolio.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        portfolios = Portfolio.objects.filter(is_active=True).prefetch_related("images").order_by("-created_at")
        return portfolios
