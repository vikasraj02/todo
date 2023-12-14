from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    task = request.POST["task"]
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_complete = True
    task.save()
    return redirect('home')

def mark_as_Undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_complete = False
    task.save()
    return redirect('home')
def Edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {'get_task': get_task}
        return render(request, 'Edit_task.html',context)
def Delete_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')