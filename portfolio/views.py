from django.shortcuts import render
from .models import Project, Technologie

def Home(request):
    projects = Project.objects.all()
    technologies = Technologie.objects.all()
    return render(request,'home.html', {'projects':projects, 'technologies':technologies})