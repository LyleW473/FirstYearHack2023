from django.urls import path
from . import views


# Paths that will connect a URL pattern to a specific path or view
urlpatterns = [
                path("", views.home, name="home"), # Base URL of website
                path("todos/", views.todos, name="todos"),
                path("add/", views.add_todo, name="add_todo_item"),
                path("clear/", views.clear_todos,name="clear_todos"),
                path("remove/<int:todo_id>/", views.remove_todo, name="remove_todo_item")
                ]