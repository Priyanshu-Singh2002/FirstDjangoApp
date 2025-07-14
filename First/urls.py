"""
URL configuration for First project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from home.views import *
from recipe.views import *
# from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('send-email/',Send_a_email,name='Send_a_email'),
    path('about/',about, name = 'about'),
    path('contact/',contact,name='contact'),
    path('recipe/',add_recipe, name='add_recipe'),
    path('recipe/delete/<int:id>/',delete_recipe, name='delete_recipe'),
    path('recipe/update/<int:id>/', update_recipe, name='update_recipe'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register, name='register'),
    path('student/', get_student, name='get_student'),
    path('student/reportcard/<str:id>',get_student_report,name='get_student_report')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()