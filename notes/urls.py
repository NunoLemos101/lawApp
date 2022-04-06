from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('notes.api.v1.urls'))
]


