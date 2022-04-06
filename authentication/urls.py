from django.urls import path, include

from authentication.api.v1.rest_auth.views import CustomUserDetailsView
from authentication.api.v1.override import CustomLoginView, CustomRegisterView

urlpatterns = [
    path('api/v1/rest-auth/login/', CustomLoginView.as_view()),
    path('api/v1/rest-auth/registration/', CustomRegisterView.as_view()),
    path('api/v1/rest-auth/user/', CustomUserDetailsView.as_view()),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/oauth/', include('authentication.api.v1.oauth.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]