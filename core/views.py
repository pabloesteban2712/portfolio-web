from django.shortcuts import render, HttpResponse
from .models import Projects

html_base = """
<h1>My personal web</h1>
<ul>
    <li><a href="/">Home</a></li> 
    <li><a href="/resume/">Resume</a></li>
    <li><a href="/projects/">Projects</a></li>
    <li><a href="/contact/">Contact</a></li>
</ul>
"""

# Create your views here. 
def home(request):
    return render(request, "core/home.html")

def resume(request):
   return render(request, "core/resume.html")
   
def contact(request):
    return render(request, "core/contact.html")

# Create your views here.
def projects(request):
    projects = Projects.objects.all() 
    return render(request, "core/projects.html", {'projects': projects })