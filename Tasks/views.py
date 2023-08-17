from django.shortcuts import render
from django.http import HttpResponse
from . models import Task

# Create your views here.
def index(request):
    task = Task.objects.all()
    context = {
        "tasks": task
    }
    return render(request, "tasks/list.html", context=context)

