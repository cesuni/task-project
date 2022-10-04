from cProfile import label
from unittest.util import _MAX_LENGTH
from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="titulo", max_length=90)
    description = forms.CharField(label="descripcion", max_length=90)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="name", max_length=60)
