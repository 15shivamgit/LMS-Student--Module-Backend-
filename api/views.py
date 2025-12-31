from django.db import models

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



from .models import Student, Course, Assignment, Notification
from .serializers import (
    StudentSerializer, CourseSerializer,
    AssignmentSerializer, NotificationSerializer
)


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /api/students/ -> current logged-in student ki info
    """
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)


class CourseViewSet(viewsets.ModelViewSet):
    """
    /api/courses/
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentViewSet(viewsets.ModelViewSet):
    """
    /api/assignments/
    """
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Logged-in student ke assignments hi dikhao
        user = self.request.user
        try:
            student = user.student
        except Student.DoesNotExist:
            return Assignment.objects.none()
        return Assignment.objects.filter(student=student)

    def perform_create(self, serializer):
        student = self.request.user.student
        serializer.save(student=student)


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /api/notifications/
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            student = user.student
        except Student.DoesNotExist:
            student = None

        # student specific + broadcast (student=NULL)
        return Notification.objects.filter(
            models.Q(student=student) | models.Q(student__isnull=True)
        )



@method_decorator(csrf_exempt, name='dispatch')
class MyTokenObtainPairView(TokenObtainPairView):
    pass

