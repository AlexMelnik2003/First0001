from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('coc/', views.setcookie),
    path('coc2/', views.delete_coc),
]
