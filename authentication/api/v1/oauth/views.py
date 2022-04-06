from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from authentication.api.v1.override import CustomSocialLoginView


class GoogleAuth(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

