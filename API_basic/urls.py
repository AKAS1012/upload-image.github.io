from django.urls import path
from .import views


urlpatterns = [
    path('AssetAPI/', views.AssetAPI.as_view()),
    path('AssetAPI/<int:pk>/', views.AssetAPI.as_view()),
]
