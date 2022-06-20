from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', views.OrderDetail.as_view()),
    path('', views.OrderList.as_view()),
    #path('<int:pk>/', views.single_order_page),
    #path('', views.index),
]