from django.shortcuts import render, HttpResponse, redirect
from .models import ToDoItem
from .forms import ToDoItemForm


# Create your views here.
def home(request):
    return render(request=request, template_name="home.html") # Return html template

def todos(request):
    items = ToDoItem.objects.all() # Get all instances of ToDoItem in the database
    return render(request=request, template_name="todos2.html", context = {"todos": items})

def add_todo(request):
    if request.method == "POST":
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Item added successfully", status=200)
    # Return empty response
    return HttpResponse(status=200)

def clear_todos(request):
    ToDoItem.objects.all().delete() # Delete all ToDoItem objects
    return redirect("todos")