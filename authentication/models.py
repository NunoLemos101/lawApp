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