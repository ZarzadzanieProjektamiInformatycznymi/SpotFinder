from django.urls import path
from . import views

urlpatterns = [
    path('', views.spot_list, name='spot_list'),
    path('spot/<int:pk>/', views.spot_detail, name='spot_detail'),
    path('spot/new/', views.spot_create, name='spot_create'),
    path('spot/<int:pk>/edit/', views.spot_update, name='spot_update'),
    path('spot/<int:pk>/delete/', views.spot_delete, name='spot_delete'),
]