from django.db import models
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    aficion = models.CharField(max_length=50)