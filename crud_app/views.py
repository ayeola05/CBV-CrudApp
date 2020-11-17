from django.shortcuts import render
from crud_app.models import School
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.
class Index(TemplateView):
  template_name = 'crud_app/index.html'

class SchoolList(ListView):
  model = School

class SchoolDetail(DetailView):
  model = School

class SchoolUpdate(UpdateView):
  model = School
  fields = '__all__'

class SchoolCreate(CreateView):
  model = School
  fields = '__all__'

class SchoolDelete(DeleteView):
  model = School
  context_object_name = 'school_delete'
  success_url = reverse_lazy('crud_app:list')
