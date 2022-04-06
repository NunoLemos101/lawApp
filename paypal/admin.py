from django.contrib import admin
from paypal.models import AfterPaymentToken, BeforePaymentToken

admin.site.register(AfterPaymentToken)
admin.site.register(BeforePaymentToken)

# Register your models here.


