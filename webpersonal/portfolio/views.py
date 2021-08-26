from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Project
from django.db.models.query import QuerySet
# Create your views here.
def portfolio(request: WSGIRequest) -> render:
    projects: QuerySet = Project.objects.all()
    print(projects.count())
    return render(request, 'portfolio/portfolio.html', context={'projects': projects})