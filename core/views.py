from django.shortcuts import render
from django.views.generic import TemplateView
#INICIO
class HomeView(TemplateView):
    template_name = 'home.html'
