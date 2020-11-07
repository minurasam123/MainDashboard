from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Course, Level
from .forms import StudentCreationForm
from django.contrib import messages


# ------------------general Views-----------------------


def home(request):
    return render(request, 'General/general.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return render(request, 'admin/admin.html')
            else:
                return render(request, 'Student/student_dashboard.html')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def register(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/SignUpPage.html', context)


def courses(request):
    return render(request, 'General/courses.html')


def cert(request):
    return render(request, 'Genera l/certificateLevel.html')


def op(request):
    return render(request, 'General/operational_level.html')


def mgt(request):
    return render(request, 'General/managementlevel.html')


def strat(request):
    return render(request, 'General/strategic_level.html')


# ------------------Admin Views----------------------

def admin(request):
    return render(request, 'admin/admin.html')


def all_student_info(request):
    return render(request, 'admin/All Student information.html')


def view_courses(request):
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)

    return render(request, 'admin/view_courses.html', {'courses': courses})


def content(request):
    return render(request, 'admin/content.html')


def drop_lectures(request):
    return render(request, 'admin/Drop Lectures.html')


def lecture_notes(request):
    return render(request, 'admin/lecture_notes.html')


def student_profile(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'admin/stdprofile.html', {'students': students})


def student_details(request):
    return render(request, 'admin/Student Details.html')


def student_edit(request):
    levels = Level.objects.all()
    return render(request, 'admin/StuEdit.html', {'levels': levels})


def load_course(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    course = Course.objects.filter(level_id=user).order_by('name')
    d = {'course': course}
    return render(request, 'admin/course_dropdown.html', d)


def stud_data(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    students = Student.objects.filter(level=user)
    d = {'students': students}
    return render(request, 'admin/studentdata.html', d)


# -----------------------Student views---------------------


def student_form(post):
    return render(post, 'Student/form.html')


def std_profile(request):
    return render(request, 'Student/profile.html')


def std_lectures(request):
    return render(request, 'Student/student_my_lectures.html')


def student(request):
    return render(request, 'Student/student_dashboard.html')


def dashboard(request):
    return render(request, "users/dashboard.html")
