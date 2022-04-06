from django.urls import path, include
from . import views

urlpatterns = [
    path('custom-admin-api/', include('customAdmin.api.urls')),
    path('login/', views.dashboard, {'id': None}),
    path('custom-admin/', views.dashboard, {'id': None}),
    path('custom-admin/dashboard/', views.dashboard, {'id': None}),
    path('custom-admin/devices/', views.dashboard, {'id': None}),
    path('custom-admin/categories/', views.dashboard, {'id': None}),
    path('custom-admin/categories/<int:id>/', views.dashboard),
    path('custom-admin/account/', views.dashboard, {'id': None}),
    path('custom-admin/settings/', views.dashboard, {'id': None}),

]


