from django.shortcuts import render
from . import models


def index(request):
    if request.method == 'POST':
        task = models.Post()
        task.task = request.POST['text']
        task.save()
        return render(request, 'index.html')
    return render(request, 'index.html')

def task(request):
    work = models.Post.objects.all()
    return render(request, 'task.html', {'work': work})
# Create your views here.
