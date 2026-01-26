from django.urls import path 
import app1.views as views

urlpatterns = [
    path('message/', views.SimpleReponseView.as_view()),
    path('hello/', views.hello_worlds),
    path('render/', views.how_render_works_drf),
]