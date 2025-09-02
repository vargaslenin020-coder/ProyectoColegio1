# estudiantes/models.py

from django.db import models

class Estudiante(models.Model): # <-- ¡Asegúrate que el nombre sea "Estudiante"!
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"