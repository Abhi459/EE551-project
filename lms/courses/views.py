from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Course
from .models import Student
from .models import Announcement
from .models import Assignment
from .models import Grade

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def courses(request):
    user_id = request.user.id
    course_ids = Student.objects.filter(student_id=user_id)
    list_course_ids = []
    for id in course_ids.iterator():
        list_course_ids.append(str(id.student_course_id))
    courses = Course.objects.filter(course_id__in=list_course_ids)
    print(courses)
    values = ['bg-primary', 'bg-secondary', 'bg-info', 'bg-dark']
    return render(request, 'courses.html', {'courses': courses, 'value': values})

@login_required(login_url='/login')
def course_details(request, id):
    course_id = id
    course = Course.objects.get(course_id=course_id)

    # Get announcements in a course
    announcements = Announcement.objects.filter(announcement_in_course=course_id)

    # Get all students enrolled in the course
    student_ids = Student.objects.filter(student_course_id=course_id)
    list_of_students = []
    # for id in student_ids.iterator():
    #     student_course_ids.append(str(id.student_id))
    for student in student_ids:
        list_of_students.append(student.student_id)

    # Get assignments
    files = Assignment.objects.filter(file_belongs_to_course=course_id)

    # Get grades
    grades = Grade.objects.filter(user_id=request.user.id)

    return render(request, 'course_details.html', {'course': course,'course_id': course_id, 'announcements': announcements, 'students': list_of_students, 'assignments': files, 'grades': grades})