from django.utils import timezone

from django.db import models

# Create your models here.


class Statistics(models.Model):
    brute_income = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    liquid_income = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    paypal_commissions = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return 'Brute Income: {}€ | Liquid Income: {}€ | PAYPAL Comissions: {}€'.format(self.brute_income, self.liquid_income, self.paypal_commissions)


class DailyStatistics(models.Model):
    """
    A new object of this class is created every 24h at midnight
    """
    article_entries = models.PositiveIntegerField(default=0)
    personal_notes_edited = models.PositiveIntegerField(default=0)
    personal_notes_created = models.PositiveIntegerField(default=0)
    personal_notes_entries = models.PositiveIntegerField(default=0)
    mobile_api_requests = models.PositiveIntegerField(default=0)
    app_launched_count = models.PositiveIntegerField(default=0)
    new_devices = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    @staticmethod
    def get_today_model():
        return DailyStatistics.objects.filter(creation_date__year=timezone.now().year, creation_date__month=timezone.now().month, creation_date__day=timezone.now().day)[0]

    def __str__(self):
        return '{}/{}/{}'.format(self.creation_date.day, self.creation_date.month, self.creation_date.year)