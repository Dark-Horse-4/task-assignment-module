"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from todo_view import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView , name='home'),
    path('sign-up/', views.SignUp , name='signup'),
    path('sign-in/', views.SignInView.as_view() , name='signin'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='todo_view/sign-out.html'), name= 'signout'),
    path('new-task/', views.TaskCreateView.as_view() , name='newtask'),
    path('my-task/', views.MyTaskList , name='mytask'),
    path('complete-task/<int:id>', views.CompletedTaskList , name='completedtask'),
    path('done-task/', views.CompletedList , name='donetask'),
    path('user-task/<int:id>', views.UserTaskList , name='usertask'),
    path('update-image/', views.UploadPic , name='uploadimage'),
    #path('assignee_autocomp/', views.assignee_autocomplete , name='autocomplete'),
    #path('assignee-autocomplete/',views.get_Assignee,name='assignee-autocomplete'),
    
] 


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
