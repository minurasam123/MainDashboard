from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Student, Course, Level, Module, Content, Lecturer
from .forms import StudentCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.views.generic.list import ListView
from .forms import CourseCreationForm
from django.forms.models import modelform_factory
from django.apps import apps
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet


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
            cima_id = form.cleaned_data.get('Cima_ID')

            group = Group.objects.get(name='Student')
            user.groups.add(group)
            Student.objects.create(
                user=user,
                Cima_ID = cima_id,
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
@allowed_users(allowed_roles=['Lecturer'])
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
    context = {'courses': courses}
    return render(request, 'admin/view_courses.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def create_course(request):
    form = CourseCreationForm()
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('v_courses')

    context = {'form': form}
    return render(request, 'admin/create_course.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseCreationForm(instance=course)

    if request.method == 'POST':
        form = CourseCreationForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('v_courses')

    context = {'form': form}
    return render(request, 'admin/create_course.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        return redirect('v_courses')
    context = {'course': course}
    return render(request, 'admin/delete_courses.html', context)


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
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)
    level1 = courses.filter(level=7)
    level2 = courses.filter(level=2)
    level3 = courses.filter(level=5)
    level4 = courses.filter(level=6)
    context = {'course': courses,
               'level1': level1,
               'level2': level2,
               'level3': level3,
               'level4': level4}
    return render(request, 'admin/lecture_notes.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_profile(request):
    users = request.user
    lecturer = Lecturer.objects.get(user=users)
    students = Student.objects.filter(lecturer=lecturer.id).order_by('id')
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


# ------------------Content Management--------------------------


class ManageCourseListView(ListView):
    model = Course
    template_name = 'admin/manage/content_list.html'

    def get_queryset(self):
        qs = super(ManageCourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'admin/manage/module_form.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course,
                             data=data)

    def dispatch(self, request, pk):
        user = request.user
        self.course = get_object_or_404(Course,
                                        id=pk,
                                        lecturer=user.lecturer)
        return super(CourseModuleUpdateView,
                     self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('addNotes')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'admin/manage/content_form.html'

    def get_model(self, model_name):
        if model_name in ['video', 'image', 'file']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        user = request.user
        m_id = module_id
        self.module = get_object_or_404(Module, id=m_id, course__owner=user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super(ContentCreateUpdateView, self).dispatch(request, m_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance=self.obj,
                             data=request.POST,
                             files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                # new content
                Content.objects.create(module=self.module,
                                       item=obj)
            return redirect('module_content_list', self.module.id)

        return self.render_to_response({'form': form,
                                        'object': self.obj})
