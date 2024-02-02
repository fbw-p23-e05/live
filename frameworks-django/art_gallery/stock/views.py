from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def listings(request):
    return HttpResponse("<ol><li>Maksym</li><li>Monica</li><li>Shilpa</li></ol>")
