from django.urls import path
from . import views

# Paths that will connect a URL pattern to a specific path or view
urlpatterns = [
                path("", views.home, name="home"), # Base URL of website
                path("todos/", views.todos, name="todos")
                ]