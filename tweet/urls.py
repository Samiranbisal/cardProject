from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet, name='tweet'),
    path('sb/', views.sb),
]
