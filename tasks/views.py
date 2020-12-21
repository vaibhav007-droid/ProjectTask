from idlelib.searchengine import get
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.views.generic.edit import UpdateView

from django.contrib.auth import get_user_model

User = get_user_model()


class TaskList(SelectRelatedMixin, generic.ListView):
    model = models.Task
    select_related = ('user', 'project')


class UserTask(generic.ListView):
    model = models.Task
    template_name = 'tasks/user_task_list.html'

    def get_queryset(self):
        try:
            self.task_user = User.objects.prefetch_related('task').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.task_user.task.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_user'] = self.task_user
        return context


class TaskDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Task
    select_related = ('user', 'project')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreateTask(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('name', 'description', 'start_date', 'end_date', 'project')
    model = models.Task

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Task
    select_related = ('user', 'project')
    success_url = reverse_lazy('task:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Task Deleted')
        return super().delete(*args, **kwargs)


class Update(UpdateView):
    model = models.Task  # model
    fields = ['name', 'description']  # fields / if you want to select all fields, use "__all__"
    template_name = 'tasks/task_confirm_update.html'  # templete for updating
    success_url = reverse_lazy('task:all')  # posts list url
