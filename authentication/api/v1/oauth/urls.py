from django.urls import path

from authentication.api.v1.oauth.views import GoogleAuth

urlpatterns = [
    path('google/', GoogleAuth.as_view(), name='google-auth')
]