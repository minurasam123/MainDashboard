from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
# from django.contrib.auth.models import User


class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    level_No = models.IntegerField(null=True)
    level_name = (
        ("Certificate Level", "Certificate Level"),
        ("Operational Level", "Operational Level"),
        ("Management Level", "Management Level"),
        ("Strategic Level", "Strategic Level")
        )
    level = models.CharField(choices=level_name, max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.level


class Student(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    Cima_ID = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Course(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    course_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=255)
    overview = models.TextField()
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.module_name)


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': (
                            'text',
                            'video',
                            'image',
                            'file'
                        )
            },
        on_delete=models.CASCADE
        )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    r = '%(class)s_related'
    lec = models.ForeignKey(Lecturer, related_name=r, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
