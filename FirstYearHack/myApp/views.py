from django.shortcuts import render, HttpResponse
from .models import ToDoItem

# Create your views here.
def home(request):
    return render(request=request, template_name="home.html") # Return html template

def todos(request):
    items = ToDoItem.objects.all() # Get all instances of ToDoItem in the database
    return render(request=request, template_name="todos.html", context = {"todos": items})