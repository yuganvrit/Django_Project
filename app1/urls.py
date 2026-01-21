from django.urls import path 
import app1.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),

]