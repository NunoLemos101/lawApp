from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import RegisterView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.response import Response

from allauth.account.adapter import get_adapter

from dj_rest_auth.app_settings import TokenSerializer
from dj_rest_auth.views import LoginView

from authentication.api.v1.serializers import UserDetailsSerializer

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2',
    ),
)


class CustomRegisterView(RegisterView):
    """
    Overriden so that the server can return more data
    than just the REST Token when user registers
    """

    def get_response_data(self, user):
        return UserDetailsSerializer(user).data


class CustomLoginView(LoginView):
    """
    Overriden so that the server can return more data
    than just the REST Token when user authenticates
    """

    def get_response_serializer(self):
        return TokenSerializer

    def get_response(self):
        return Response(data=UserDetailsSerializer(self.request.user).data, status=200)


class CustomSocialLoginView(CustomLoginView):
    """
    Overriden so that the class could inherit
    CustomLoginView instead of LoginView
    """
    serializer_class = SocialLoginSerializer

    def process_login(self):
        get_adapter(self.request).login(self.request, self.user)
