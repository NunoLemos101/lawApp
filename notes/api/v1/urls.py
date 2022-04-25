from django.urls import path, include

urlpatterns = [
    path('', include('notes.api.v1.articles.urls')),
    path('', include('notes.api.v1.personal_notes.urls')),
    path('', include('notes.api.v1.support_tickets.urls')),
    path('', include('notes.api.v1.font_settings.urls')),
]
