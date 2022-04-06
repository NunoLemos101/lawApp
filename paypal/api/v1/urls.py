from django.urls import path

from paypal.api.v1.views import generate_payment_window, webhooks

urlpatterns = [
    path("<str:plan>/payment-window/", generate_payment_window),
    path("webhooks/", webhooks),
]