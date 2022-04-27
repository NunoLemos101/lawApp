from django.urls import include, path

from .router import CategorySettingsRouter
from .viewset import CategorySettingsViewSet
router = CategorySettingsRouter()

router.register('category-settings', CategorySettingsViewSet, basename='category-settings')

urlpatterns = [path('', include(router.urls))]
