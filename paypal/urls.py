from django.urls import path, include

urlpatterns = [
    path("api/v1/paypal/", include("paypal.api.v1.urls"))
]