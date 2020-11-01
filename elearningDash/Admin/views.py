from django.shortcuts import render
# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Course


def home(request):
    return render(request, 'General/general.html')


def courses(request):
    return render(request, 'General/courses.html')


def cert(request):
    return render(request, 'General/certificateLevel.html')


def op(request):
    return render(request, 'General/operational_level.html')


def mgt(request):
    return render(request, 'General/managementlevel.html')


def strat(request):
    return render(request, 'General/strategic_level.html')


def admin(request):
    user = request.user
    if user is not None:
        if user.is_staff:
            return render(request, 'admin/admin.html')
        else:
            return render(request, 'Student/student_dashboard.html')


def all_student_info(request):
    return render(request, 'admin/All Student information.html')


def view_courses(request):
    courses = Course.objects.all()

    return render(request, 'admin/view_courses.html', {'courses': courses})


def content(request):
    return render(request, 'admin/content.html')


def drop_lectures(request):
    return render(request, 'admin/Drop Lectures.html')


def lecture_notes(request):
    return render(request, 'admin/lecture_notes.html')


def student_profile(request):
    students = Student.objects.all()
    return render(request, 'admin/stdprofile.html', {'students': students})


def student_details(request):
    return render(request, 'admin/Student Details.html')


def student_edit(request):
    return render(request, 'admin/StuEdit.html')


def student_form(post):
    return render(post, 'Student/form.html')


def std_profile(request):
    return render(request, 'Student/profile.html')


def std_lectures(request):
    return render(request, 'Student/student_my_lectures.html')


def student(request):
    return render(request, 'Student/student_dashboard.html')
