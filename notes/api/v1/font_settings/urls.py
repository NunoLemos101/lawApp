from django.urls import include, path

from .router import FontSettingsRouter
from .viewset import FontSettingsViewSet
router = FontSettingsRouter()

router.register('font-settings', FontSettingsViewSet, basename='font-settings')

urlpatterns = [path('', include(router.urls))]
