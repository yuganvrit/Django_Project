from django.urls import path 
import app1.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),

]