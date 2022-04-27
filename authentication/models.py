from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

DEFAULT_CATEGORY_SETTINGS = [
    {
        "id": 0,
        "title": "Área Civil",
        "themeColor": "#42C6A5",
        "codigos": ["cc", "cpc", "crp", "crcivil"],
        "thumbnail": "BG_1"
    },
    {
        "id": 1,
        "title": "Área Penal",
        "themeColor": "#E5C184",
        "codigos": ["cp", "cpp", "rgit"],
        "thumbnail": "BG_2"
    },
    {
        "id": 2,
        "title": "Administrativo",
        "themeColor": "#98A6EF",
        "codigos": ["cpa", "cpta"],
        "thumbnail": "BG_3"
    },
    {
        "id": 3,
        "title": "Trabalho",
        "codigos": ["ct", "cpt"],
        "themeColor": "#64BEE1",
        "thumbnail": "BG_4"
    },
    {
        "id": 4,
        "title": "Comercial",
        "themeColor": "#657286",
        "codigos": ["csc", "crcomercial", "ncpi", "cvm"],
        "thumbnail": "BG_6"
    },
    {
        "id": 5,
        "title": "Fiscal",
        "themeColor": "#98A6EF",
        "codigos": ["lgt", "cppt", "rgit"],
        "thumbnail": "BG_3"
    },
    {
        "id": 6,
        "title": "Outros",
        "themeColor": "#FC9BA1",
        "codigos": ["ce"],
        "thumbnail": "BG_5"
    },
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    category_settings = models.JSONField(default=DEFAULT_CATEGORY_SETTINGS)

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
        ("normal", "normal"),
        ("bold", "bold")
    ]

    FONT_STYLE_CHOICES = [
        ("normal", "normal"),
        ("italic", "italic")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    font_family = models.TextField(default="Roboto-Regular")
    font_size = models.IntegerField(default=14)
    font_color = models.TextField(default="#7F7F7F")
    background_color = models.TextField(default="#FFFFFF")
    font_weight = models.CharField(max_length=6, choices=FONT_WEIGHT_CHOICES, default="normal")
    font_style = models.CharField(max_length=6, choices=FONT_STYLE_CHOICES, default="normal")

    def serialize(self):
        return {
            "fontFamily": self.font_family,
            "fontSize": self.font_size,
            "lineHeight": self.font_size,
            "color": self.font_color,
            "backgroundColor": self.background_color,
            "fontWeight": self.font_weight,
            "fontStyle": self.font_style
        }
