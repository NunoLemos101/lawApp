from dj_rest_auth.views import UserDetailsView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from authentication.api.v1.serializers import UserDetailsSerializer

User = get_user_model()


class CustomUserDetailsView(UserDetailsView):

    serializer_class = UserDetailsSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request)
