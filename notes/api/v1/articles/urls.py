from django.urls import include, path

from .router import ArticleRouter
from .views import ArticleViewSet

router = ArticleRouter()

router.register('articles', ArticleViewSet, basename='articles')

# /api/v1/devices/ [POST]
# /api/v1/articles/{id}/ [GET]
urlpatterns = [path('', include(router.urls))]
