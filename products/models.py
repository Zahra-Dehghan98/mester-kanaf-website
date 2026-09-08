from django.db import models

class Product(models.Model):
    UNIT_CHOICES = [
        ('m2', 'مترمربع'),
        ('unit', 'عدد'),
        ('kg', 'کیلوگرم'),
        ('pack', 'بسته'),
        ('roll', 'رول'),
    ]
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="تصویر")
    price = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, verbose_name="قیمت (تومان)")
    unit = models.CharField(choices=UNIT_CHOICES, verbose_name="واحد")
    order = models.IntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return self.title
