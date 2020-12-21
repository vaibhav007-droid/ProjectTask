# Project urls.py File

from django.urls import path, include
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.ListProjects.as_view(), name='all'),
    path('new/', views.CreateProject.as_view(), name='create'),
    path('task/in/(?P<slug>[-\w]+)/', views.SingleProject.as_view(), name='single'),
    path('join/(?P<slug>[-\w]+)/', views.JoinProject.as_view(), name='join'),
    path('leave/(?P<slug>[-\w]+)/', views.LeaveProject.as_view(), name='leave'),
]
