from django.shortcuts import render
from .import models
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.
class Index(TemplateView):
  template_name = 'crud_app/index.html'

class SchoolList(ListView):
  model = models.School

class SchoolDetail(DetailView):
  model = models.School

class SchoolUpdate(UpdateView):
  model = models.School
  fields = '__all__'

class SchoolCreate(CreateView):
  model = models.School
  fields = '__all__'

class SchoolDelete(DeleteView):
  model = models.School
  context_object_name = 'school_delete'
  success_url = reverse_lazy('crud_app:list')
