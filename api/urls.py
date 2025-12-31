from django.urls import path, include
from rest_framework import routers



from .views import StudentViewSet, CourseViewSet, AssignmentViewSet, NotificationViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
]





