from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def todo_list(request):
    return render(request, "todo/todo_list.html")
    # return render(request, "todo_list2.html")

# def todo_list(request):
#     return HttpResponse("Hello World")
