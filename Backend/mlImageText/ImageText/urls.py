from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('image/', views.getImages, name="ImageText"),
    path('text/', views.getTexts, name="ImageText"),
    path('image/<str:pk>', views.getImage, name="ImageText"),
    path('text/<str:pk>', views.getText, name="ImageText"),
]
