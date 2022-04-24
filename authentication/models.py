from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def is_trial_over(self):
        if timezone.now() > self.user.date_joined + timedelta(days=settings.TRIAL_PERIOD):
            return True
        return False

    def has_access(self):
        if self.is_premium or not self.is_trial_over():
            return True
        return False


class FontSettings(models.Model):

    FONT_WEIGHT_CHOICES = [
        ("NORMAL", "normal"),
        ("BOLD", "bold")
    ]

    FONT_STYLE_CHOICES = [
        ("NORMAL", "normal"),
        ("ITALIC", "italic")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    font_family = models.TextField(default="Roboto-Regular")
    font_size = models.IntegerField(default=14)
    font_color = models.TextField(default="#7F7F7F")
    font_weight = models.CharField(max_length=6, choices=FONT_WEIGHT_CHOICES, default="NORMAL")
    font_style = models.CharField(max_length=6, choices=FONT_STYLE_CHOICES, default="NORMAL")

    def serialize(self):
        return {
            "fontFamily": self.font_family,
            "fontSize": self.font_size,
            "lineHeight": self.font_size,
            "color": self.font_color,
            "fontWeight": self.font_weight,
            "fontStyle": self.font_style
        }
