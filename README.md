# Introduction:

This is EE551 Python project By <i>**Abhishek Lokam**</i>

## Proposal:

This project provides Website using Django Framework that is similar to canvas website. There will only some features of the
canvas site.

### Features:

1. Login functionality for both Professors (as Admin) and for students

2. Admin site displays the following:

  * <i>**Dashboard**</i>: Display the courses to which the admin is linked to.
  * <i>**Files Sections**</i>: able to add and retrieve files from the system.
  * <i>**People section**</i>: able to add a student to the course.
  * <i>**Assignment section**</i>: able to post assignments. Include Due date
      feature as well.
  * <i>**Grade section**</i>: able to post grades. 

3. Student has access to the following: 

  * <i>__Dashboard__</i>: Display the current courses taken by the student.
  * <i>__Files section__</i>:  Retrieve files from the system added by the
      admin.
  * <i>__Peoples section__</i>: able to view the people present in the course.
  * User will be able to view the grades for the course.

# Usage:

1. First start an virtual environment 
2. Requirements python 3, Django(pip install django), widget-tweaks(pip install django-widget-tweaks)
3. Go the project folder and go to lms folder
4. use command python manage.py createsuperuser to create admin(professor)
5. use command python manage.py runserver to start
6. New users can register using sign up form
7. Admin can access site using Ipaddress/admin
8. In the admin site, the admin can add students to the course,create courses etc.

