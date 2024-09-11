"""
URL configuration for reddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# reddy/urls.py

from django.contrib import admin
from django.urls import path
from student import views  # Import views from 'student' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),        # Home page URL
    path('services/', views.services, name='services'),  # Services page URL
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('register/', views.register, name='register'),  # Register page
    path('student-database/', views.student_database, name='student_database'),
]


