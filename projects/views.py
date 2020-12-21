from sqlite3.dbapi2 import IntegrityError

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from projects.models import Project, ProjectTask
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import models


class CreateProject(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description', 'duration', 'avatar')
    model = Project


class SingleProject(generic.DetailView):
    model = Project


class ListProjects(generic.ListView):
    model = Project


class JoinProject(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('project:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, slug=self.kwargs.get('slug'))
        try:
            ProjectTask.objects.create(user=self.request.user, project=project)
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'You are now a member')
        return super().get(request, *args, **kwargs)


class LeaveProject(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('project:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            tasks = models.ProjectTask.objects.filter(
                user=self.request.user,
                project__slug=self.kwargs.get('slug')
            ).get()
        except models.ProjectTask.DoesNotExist:
            messages.warning(self.request, "Sorry You Are not Assign Project")
        else:
            tasks.delete()
            messages.success(self.request, "You Are Leave The Project")
        return super().get(request, *args, **kwargs)
