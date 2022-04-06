from django.urls import include, path

from .router import PersonalNoteRouter
from .views import PersonalNoteViewSet

router = PersonalNoteRouter()

router.register('personal-notes', PersonalNoteViewSet, basename='personal-notes')

# /api/v1/personal-notes/ [POST | GET | DELETE]
# /api/v1/personal-notes/{id}/ [GET | PUT]
urlpatterns = [path('', include(router.urls))]
