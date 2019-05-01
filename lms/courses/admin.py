from django.contrib import admin
from .models import Course
from .models import Student
from .models import Announcement
from .models import Assignment
from .models import Grade

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(Grade)