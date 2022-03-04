from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        task = models.Post()
        task.task = request.POST['text']
        if models.Post.objects.filter(task = task).exists():
            messages.info(request, 'task already exist')
            return redirect('index')
        else:
            task.save()
            messages.info(request, 'task is added')
            return render(request, 'index.html')
    return render(request, 'index.html')

def task(request):
    work = models.Post.objects.all()
    return render(request, 'task.html', {'work': work})

def detail(request, pick):
    work = models.Post.objects.get(id = pick )
    return render(request, 'detail.html', {'works':work})
