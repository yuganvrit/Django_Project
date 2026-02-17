from django.urls import path,include
import app1.views as views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'course',views.CourseViewset)
router.register(r'generic-student',views.StudentGenericView)





urlpatterns = [
    # path('echo-data/', views.echo_data, name='echo_data'),
    # path('show-headers-params/', views.show_request_details, name='show_headers'),
    # path('filter-items/', views.filter_items, name='filter_items'),
    # path('display-student/', views.display_student_data, name='display-student'),
    # path('create-student/', views.create_student_data, name='create_student'),
    path('student/', views.get_or_create_student, name='get_or_create_student'),
    path('books-author/', views.create_books_with_author, name='create_books_with_author'),
    path('users/', views.register_user, name='users'),
    path('users/login', views.login_user, name='login_users'),
    path('hello-world/', views.simple_hello_world, name='hello-world'),
    path('class-based-view/',views.NormalClassBasedView.as_view(),name='class-based-view'),
    path('delete-student/<int:pk>/',views.DeleteOrUpdateStudentView.as_view(),name='delete-student'),
    path('',include(router.urls))
]


