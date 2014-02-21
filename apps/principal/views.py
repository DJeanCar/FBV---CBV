from django.shortcuts import render
from .forms import PersonaForm
from django.views.generic import CreateView,ListView,DetailView
from .models import Persona


def CrearFBV(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PersonaForm()
	return render(request, 'crear_FBV.html',
				{'form':form})

def ListarFBV(request):
	personas = Persona.objects.all()
	return render(request, 'listar_FBV.html',
				{'personas' : personas})


class ListarCBV(ListView):
	model = Persona
	template_name = 'listar_CBV.html'

class CrearCBV(CreateView):
	template_name = 'crear_CBV.html'
	model = Persona
	success_url = '/'

class DetalleCBV(DetailView):
	model = Persona
	template_name = 'detalle_CBV.html'