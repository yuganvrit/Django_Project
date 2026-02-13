from rest_framework.routers import DefaultRouter
from app1 import views

router = DefaultRouter()

router.register('course/',views.CourseViewset,basename='course')

