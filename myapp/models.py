from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=60)

    # cambiar la vista de los valores en admin
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyect = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name + ' - ' + self.proyect.name
