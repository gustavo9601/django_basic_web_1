from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse


def test(request: WSGIRequest) -> HttpResponse:
    print(request.get_host())
    return HttpResponse(f"Esto es un test desde {request.path}")


def home(request: WSGIRequest) -> render:
    return render(request, 'core/home.html')


def about(request: WSGIRequest) -> render:
    return render(request, 'core/about.html')


def contact(request: WSGIRequest) -> render:
    return render(request, 'core/contact.html')



