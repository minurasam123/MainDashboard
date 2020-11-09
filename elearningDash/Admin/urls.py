from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('courses', views.courses, name='courses'),
    # ---------------------------------------------------------
    path('courses/certificate_level/', views.cert, name='cert'),
    path('courses/operational_level/', views.op, name='oper'),
    path('courses/management_level/', views.mgt, name='mgt'),
    path('courses/strategic_level/', views.strat, name='strat'),
    # ---------------------------------------------------------
    path('accounts/prof/', views.admin, name='admin'),
    path('accounts/prof/courses', views.view_courses, name='v_courses'),
    path('account/prof/create-couses', views.create_course, name='c_course'),
    path('accounts/prof/content', views.content, name='lecnotesvids'),
    path('accounts/prof/editstudent', views.student_edit, name='edit_stud'),
    path('accounts/prof/es/cs', views.load_course, name='courses_dropdown'),
    path('accounts/prof/es/cs1', views.stud_data, name='std_list'),
    path('accounts/prof/lec_notes', views.lecture_notes, name='addNotes'),
    path('accounts/prof/students', views.student_profile, name='v_students'),
    # ----------------------------------------------------------------------------
    path('accounts/stud_prof/', views.student, name='student'),
    path('accounts/stud_prof/dashboard', views.stud_dash, name='dashboard'),
]