from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings



class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    admission_no = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admission_no} - {self.full_name}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    instructor = models.CharField(max_length=200)
    credits = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Assignment(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_file = models.FileField(upload_to='assignments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    TYPE_CHOICES = (
        ('deadline', 'Deadline'),
        ('event', 'Event'),
        ('message', 'Message'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='notifications',
        blank=True,
        null=True,
        help_text="Null means broadcast to all students."
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    from_who = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='message')
    urgent = models.BooleanField(default=False)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title
