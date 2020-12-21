# TASK models.py File
import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka

from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False)
    start_date = models.CharField(max_length=255, blank=True)
    end_date = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(Project, related_name='project', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task:single', kwargs={'username': self.user.username,
                                              'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'description']
