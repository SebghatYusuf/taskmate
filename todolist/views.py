from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import TaskList
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    print('inside index')
    return render(request, 'index.html', {})


@login_required
def todolist(request):
    if request.method == "POST":
        print(request.method, request.POST)
        if request.POST.get('task') == '':
            messages.warning(request, ("Empty input, please enter something. "))
            return redirect('todo-list')
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        messages.success(request, ("New Task Added"))
        return redirect('todo-list')
    else:

        all_tasks = TaskList.objects.filter(user=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {"all_tasks": all_tasks})


@login_required
def contact(request):
    context = {}
    return render(request, 'contact.html', context)


@login_required
def about(request):
    context = {}
    return render(request, 'about.html', context)


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user == request.user:
        task.delete()
        messages.warning(request, (f"{task.task} Deleted!"))
        return redirect("todo-list")
    else:
        messages.warning(request, ("Your Not Allowed!"))
        return redirect('todo-list')


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user == request.user:
        task.done = True
        task.save()
        return redirect("todo-list")
    else:
        messages.warning(request, ("Your Not Allowed!"))
        return redirect('todo-list')


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("todo-list")


@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))
        return redirect('todo-list')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit_task.html', {"task": task})
