from django.contrib import admin
from . import models


# Register your models here.
class ProjectMemberInline(admin.TabularInline):
    model = models.ProjectTask


admin.site.register(models.Project)
