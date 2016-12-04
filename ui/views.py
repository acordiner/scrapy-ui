from django.shortcuts import render
from django.views.generic import TemplateView


def schedule(request):
    return TemplateView.as_view(template_name='ui/project.html')
