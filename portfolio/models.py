from django.db import models


class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('residential', 'مسکونی'),
        ('commercial', 'تجاری'),
    ]
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True, verbose_name="تصویر")
    category  = models.CharField(choices=CATEGORY_CHOICES, verbose_name="دسته بندی")
    order = models.IntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="images", verbose_name="پروژه")
    image = models.ImageField(upload_to="portfolio/gallery/", blank=True, null=True, verbose_name="تصویر")
    order = models.IntegerField(default=0, verbose_name="ترتیب")

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f'تصویر برای {self.portfolio.title}'