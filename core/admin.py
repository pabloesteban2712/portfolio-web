from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Projects

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonlyfields = ('created', 'updated')



admin.site.register(Projects, ProjectAdmin)