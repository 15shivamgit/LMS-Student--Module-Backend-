from django.contrib import admin
from .models import Student, Course, Assignment, Notification

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'full_name', 'course_name', 'year')
    search_fields = ('admission_no', 'full_name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'instructor', 'credits')
    search_fields = ('code', 'title', 'instructor')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'course', 'due_date', 'status')
    list_filter = ('status', 'course')
    search_fields = ('title',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_who', 'type', 'urgent', 'date')
    list_filter = ('type', 'urgent')
    search_fields = ('title', 'from_who')
