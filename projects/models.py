# PROJECT models.py File

from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()
from django import template

register = template.Library()


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    duration = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='ProjectTask')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class ProjectTask(models.Model):
    project = models.ForeignKey(Project, related_name='task', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_task', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('project', 'user')
