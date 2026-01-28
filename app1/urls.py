from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('filter/', views.filter, name="filter"),
]
