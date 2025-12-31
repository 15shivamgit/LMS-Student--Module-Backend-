from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Course, Assignment, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )

    class Meta:
        model = Assignment
        fields = [
            'id', 'student', 'course', 'course_id', 'title', 'description',
            'due_date', 'status', 'submitted_file', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'student']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
