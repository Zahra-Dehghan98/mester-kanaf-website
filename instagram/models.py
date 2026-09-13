from django.db import models

class Instagram(models.Model):
    image = models.ImageField(upload_to="instagram/", verbose_name="کاور پست")
    link = models.URLField(verbose_name="لینک پست")
    order = models.IntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
