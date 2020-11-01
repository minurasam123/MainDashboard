from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('courses/certificate_level/', views.cert, name='cert'),
    path('courses/operational_level/', views.op, name='oper'),
    path('courses/management_level/', views.mgt, name='mgt'),
    path('courses/strategic_level/', views.strat, name='strat'),
    path('accounts/profile/', views.admin, name='admin'),
    path('accounts/profile/courses', views.view_courses, name='v_courses'),
    path('accounts/profile/content', views.content, name='lecnotesvids'),
    path('accounts/profile/editstudent', views.student_edit, name='edit_stud'),
    path('accounts/profile/lec_notes', views.lecture_notes, name='addNotes'),
    path('accounts/profile/students', views.student_profile, name='v_students')
]