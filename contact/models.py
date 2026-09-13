from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    subject = models.CharField(max_length=100, blank=True, null=True, verbose_name="موضوع پیام")
    message = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    def __str__(self):
        return str(self.phone)