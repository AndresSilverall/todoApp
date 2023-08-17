from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from. forms import TaskForm

# Create your views here.
def index(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    context = {
        "tasks": task,
        "form": form
    }
    return render(request, "tasks/list.html", context=context)

