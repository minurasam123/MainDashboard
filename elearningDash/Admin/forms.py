from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

ModuleFormSet = inlineformset_factory(Course, Module, 
                                      fields=['module_name', 
                                              'overview'], 
                                      extra=2, 
                                      can_delete=True)
