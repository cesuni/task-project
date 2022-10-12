from asyncio import tasks
from turtle import title
from urllib import request
from django.http import HttpResponse
from .forms import CreateNewProject, CreateNewTask

from myapp.forms import CreateNewTask
# importamos los modelos para realizar consultas
from .models import Project, Task
from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def index(request):
    title = 'Universidad Politecnica'
    subtitle = 'Ingenieria en software'
    return render(request, 'index.html', {
        'title': title,
        'subtitle': subtitle
    })


def about(request):
    return render(request, 'about.html')


def hello(request, username):
    return HttpResponse("<h2>this stay working %s </h2>" % username)


def project(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('Task: %s' % task.name)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        # print(request.GET['title'])
        # print(request.GET['description'])
        Task.objects.create(
            name=request.POST['title'],
            descripcion=request.POST['description'],
            proyect_id=1)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        # print(request.GET['name'])
        Project.objects.create(
            name=request.POST['name']
        )
        return redirect('projects')
