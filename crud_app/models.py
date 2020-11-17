from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=200)
  principal = models.CharField(max_length=200)
  location = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('crud_app:detail', kwargs={'pk':self.pk})


class Student(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='student')

  def __str__(self):
    return self.name