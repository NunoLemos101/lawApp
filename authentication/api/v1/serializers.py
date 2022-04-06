from django.conf import settings
from rest_framework import serializers
from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class SocialAccountSerializer(serializers.ModelSerializer):

    extra_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SocialAccount
        fields = ("provider", "extra_data")

    def get_extra_data(self, obj):
        return json.dumps(obj.extra_data)


class UserDetailsSerializer(serializers.ModelSerializer):

    key = serializers.SerializerMethodField(read_only=True)
    social_account = serializers.SerializerMethodField(read_only=True)
    premium = serializers.SerializerMethodField(read_only=True)
    android_version_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ("key", "last_login", "date_joined", "username", "first_name", "last_name", "email", "social_account", "premium", "android_version_name")

    def get_key(self, user):
        return user.auth_token.key

    def get_social_account(self, user):
        try:
            return SocialAccountSerializer(user.socialaccount_set.get()).data
        except ObjectDoesNotExist:
            return False

    def get_premium(self, user):
        return user.profile.is_premium

    def get_android_version_name(self, user):
        return settings.BUILD_VERSION_NAME

