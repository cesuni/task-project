from asyncio import tasks
from django.urls import path
from . import views

urlpatterns = [
    path('index/',               views.index),
    path('home/',                views.home),
    path('hello/<str:username>', views.hello,),
    path('about/',               views.about,            name='about'),
    path('projects/',            views.project,          name='projects'),
    path('tasks/',               views.task,             name='tasks'),
    path('create_task/',         views.create_task,      name='create_task'),
    path('create_project/',      views.create_project,   name='create_project'),
]
