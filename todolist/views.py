from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import TaskList
from .forms import TaskForm


def todolist(request):
    if request.method == "POST":
        print(request.method, request.POST)
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added"))
        return redirect('home')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {"all_tasks": all_tasks})


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect("home")


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect("home")


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("home")


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Edited!"))
        return redirect('home')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit_task.html', {"task": task})
