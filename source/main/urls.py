"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import TasksView, OneTaskView, TaskDeleteView, TaskCreateView, \
    TaskUpdateView, multi_delete, multi_delete_task, ProjectsView, OneProjectView, ProjectCreateView, \
    ProjectUpdateView, ProjectDeleteView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/', OneProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create_view'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/multi_delete/', multi_delete, name='multi_delete'),

    path('tasks/', TasksView.as_view(), name='index'),
    path('project/<int:pk>/task/add/', TaskCreateView.as_view(), name='task_add_view'),
    path('project/<int:pk>/task/', OneTaskView.as_view(), name='task_view'),
    path('project/<int:pk>/task/delete/', TaskDeleteView.as_view(), name='task_delete_view'),
    path('project/<int:pk>/task/update/', TaskUpdateView.as_view(), name='task_update_view'),
    path('multi_delete_task/', multi_delete_task, name='multi_delete_task'),

    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]
