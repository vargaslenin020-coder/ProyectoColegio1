
from django.shortcuts import render
from .forms import EstudianteForm

def formulario_estudiante(request): 
    form = EstudianteForm()
    return render(request, 'estudiantes/formulario.html', {'form': form})