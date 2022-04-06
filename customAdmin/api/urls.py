from django.urls import path, re_path
from rest_framework.authtoken import views as restviews
from . import views


urlpatterns = [
    path('get-categories/', views.get_categories),
    path('get-detail-article/<int:article_id>/', views.get_detail_article),
    path('save-article/', views.save_article),
    path('create-article/', views.create_article),
    path('delete-article/', views.delete_article),
    path("obtain-auth-token/", restviews.obtain_auth_token),
    path("react-native-data/<int:category_id>/", views.ReactNativeDataView.as_view()),
    #pagination
    path('get-articles/<int:category_id>/', views.get_articles),
]