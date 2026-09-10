from django.db import models

class Testimonial(models.Model):
    RATING_CHOICES = [
    (5, '★★★★★ عالی'),
    (4, '★★★★ خوب'),
    (3, '★★★ متوسط'),
    (2, '★★ ضعیف'),
    (1, '★ خیلی ضعیف'),
    ]
    name = models.CharField(max_length=50, verbose_name="نام")
    message = models.TextField(verbose_name="متن نظر")
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name="امتیاز")
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False, verbose_name="تایید شده")

    def __str__(self):
        return self.name
