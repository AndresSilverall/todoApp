from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from. forms import TaskForm
import datetime

# Create your views here.
def index(request):
    created = Task.created_at
    task = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    context = {
        "tasks": task,
        "form": form,
        "time": created
    }
    return render(request, "tasks/list.html", context=context)


def update_task(request, pk: str):
    created_at = datetime.datetime.now()
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("index")

    context = {
        "update": task,
        "form": form,
        "time": created_at
    }
    return render(request, "tasks/update_tasks.html", context=context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("index")
    
    context = {"item": item }
    return render(request, "tasks/delete_item.html", context=context)
