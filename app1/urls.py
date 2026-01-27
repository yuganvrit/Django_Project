from django.urls import path 
import app1.views as views

urlpatterns = [
    path('echo-data/', views.echo_data, name='echo_data'),
    path('show-headers-params/', views.show_request_details, name='show_headers'),
    path('filter-items/', views.filter_items, name='filter_items'),
]