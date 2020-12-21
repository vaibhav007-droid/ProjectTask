from django.urls import path, include
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskList.as_view(), name='all'),
    path('new/', views.CreateTask.as_view(), name='create'),
    path('by/(?P<username>[-\w]+)', views.UserTask.as_view(), name='for_user'),
    path('by/(?P<username>[-\w]+)/(?P<pk>\d+)/', views.TaskDetail.as_view(), name='single'),
    path('delete/(?P<pk>\d+)/', views.DeleteTask.as_view(), name='delete'),
    path('update/(?P<pk>\d+)/', views.Update.as_view(), name='update'),
]
