from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=250)
    course_description = models.TextField()

    def __str__(self):
        return str(self.course_id)

class Student(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='students')
    student_course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

class Assignment(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_belongs_to_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignment')
    due_date = models.DateField(null=True)
    assignment_file = models.FileField(blank=True, null=True, upload_to="assignments/")

class Grade(models.Model):
    grades_for = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    grade = models.CharField(max_length=3)

class Announcement(models.Model):
    announcement_in_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='announcement')
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=5000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcement')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
