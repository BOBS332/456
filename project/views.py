from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, template_name='index.html')
