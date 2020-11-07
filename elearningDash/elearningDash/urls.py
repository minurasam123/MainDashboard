from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('Admin.urls')),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
