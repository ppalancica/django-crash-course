from django.http import HttpResponse
from django.shortcuts import render
from .forms import TodoForm

from .models import Todo

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # create a todo object
        pass
    context = {}
    return render(request, "todo/todo_create.html", context)

# def todo_list(request):
#     todos = Todo.objects.all()
#     print(todos)
#     return render(request, "todo/todo_list.html")


# def todo_list(request):
#     return render(request, "todo/todo_list.html")
#     # return render(request, "todo_list2.html")

# def todo_list(request):
#     return HttpResponse("Hello World")
