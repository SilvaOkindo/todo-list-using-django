from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoList


# Create your views here.
class ListListView(ListView):
    model = ToDoList
    template_name = "base.html"