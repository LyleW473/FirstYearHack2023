from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
            # return HttpResponse("Item added successfully", status=200)
    # Return empty response
    # return HttpResponse(status=200)
    return redirect("todos")

def remove_todo(request, todo_id):  
    todo = get_object_or_404(ToDoItem, id=todo_id)
    todo.delete()
    return redirect("todos")  # Redirect to the todos page after removal

def clear_todos(request):
    ToDoItem.objects.all().delete() # Delete all ToDoItem objects
    return redirect("todos")