from . import views
from django.urls import path, include

urlpatterns = [
    path('about_products/', views.about_products),
    path('', views.landing),
]