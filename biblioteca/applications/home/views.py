from django.shortcuts import render

# Create your views here.

from django.views.generic import (
  TemplateView,
  ListView,
)

class IndexView(TemplateView):
  template_name = "home/index.html"

class ListLibreria(ListView):
  template_name = "home/list.html"
  queryset = ['La sombra del viento', 'Ejercicios de estilo', 'Mejorar la productividad en 7 pasos']
  context_object_name = 'books'
