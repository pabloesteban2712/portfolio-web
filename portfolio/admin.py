from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonlyfields = ('created', 'updated')



admin.site.register(Project, ProjectAdmin)