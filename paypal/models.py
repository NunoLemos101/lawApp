from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BeforePaymentToken(models.Model):

    paypal_subscription_id = models.CharField(unique=True, max_length=128, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AfterPaymentToken(models.Model):
    """
    This Object is created when user signs the Subscription and we use this Object to keep track of which Devices are Premium
    it gathers the PayPal Subscription ID when Webhook with name BILLING.SUBSCRIPTION.ACTIVATED is received.
    then filters through BeforePaymentToken objects and gets the device public ID based on PayPal Subscription ID received above
    (Since PayPal Webhooks do not support any custom data we have to save device public ID & PayPal subscription ID beforehand)
    PS: All other recurring payments related to the same AfterPaymentToken will only extend the "expiration_date" field and create
    a new Object of type Transaction (no Device should have more than one AfterPaymentToken attached to it)
    If user cancels the Subscription and later on, activates it again, we delete old AfterPaymentToken and create a new one
    """
    PLAN_OPTIONS = [
        ('3M', '3M'),
        ('6M', '6M'),
        ('12M', '12M'),
    ]

    STATUS_OPTIONS = [
        ('ACTIVE', 'ACTIVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('CANCELED', 'CANCELED'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    given_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    email_address = models.EmailField(blank=False, unique=False)
    payer_id = models.CharField(max_length=50, unique=False, blank=True)
    plan = models.CharField(max_length=3, choices=PLAN_OPTIONS, blank=True)
    plan_id = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=9, choices=STATUS_OPTIONS, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    before_payment_token = models.OneToOneField(BeforePaymentToken, null=True, blank=True, on_delete=models.SET_NULL)