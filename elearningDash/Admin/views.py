from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, Course, Level
from .forms import StudentCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.views.generic.list import ListView
from .models import Course
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# ---------------------Authentication views-------------------------------


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('student')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register(request):
    form = StudentCreationForm()
    if request.method == 'POST':

        form = StudentCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='Student')
            user.groups.add(group)
            Student.objects.create(
                user=user,
                name=username,
                email=email
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/SignUpPage.html', context)


# ------------------general Views-----------------------


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


# ------------------Admin Views----------------------
@login_required(login_url='login')
def admin(request):
    return render(request, 'admin/admin.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def all_student_info(request):
    return render(request, 'admin/All Student information.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def view_courses(request):
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)

    return render(request, 'admin/view_courses.html', {'courses': courses})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def content(request):
    return render(request, 'admin/content.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def drop_lectures(request):
    return render(request, 'admin/Drop Lectures.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def lecture_notes(request):
    return render(request, 'admin/lecture_notes.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_profile(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'admin/stdprofile.html', {'students': students})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_details(request):
    return render(request, 'admin/Student Details.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_edit(request):
    levels = Level.objects.all()
    return render(request, 'admin/StuEdit.html', {'levels': levels})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def load_course(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    course = Course.objects.filter(level_id=user).order_by('name')
    d = {'course': course}
    return render(request, 'admin/course_dropdown.html', d)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerCourseMixin(OwnerMixin):
    model = Course


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'admin/course_delete.html'
    success_url = reverse_lazy('v_courses')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def stud_data(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    students = Student.objects.filter(level=user)
    d = {'students': students}
    return render(request, 'admin/studentdata.html', d)


# -----------------------Student views---------------------


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def student_form(post):
    return render(post, 'Student/form.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def std_lectures(request):
    return render(request, 'Student/student_my_lectures.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def student(request):
    return render(request, 'Student/profile.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def stud_dash(request):
    return render(request, 'Student/student_dashboard.html')


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        qs = super(ManageCourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user)
