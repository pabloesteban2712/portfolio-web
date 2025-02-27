from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('home/', core_views.home, name="home"),
    path('resume/', core_views.resume, name="resume"),
    path('projects/', core_views.projects, name="projects"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)