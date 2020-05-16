from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Wish
# Create your views here.
# Add the following import


# Define the home view
def home(request):
  return render(request, 'home.html')

class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'
