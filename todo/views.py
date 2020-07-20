from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def todoview (request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items' : all_todo_items})

def addTodo (request):
   new_item = TodoItem(content = request.POST['content'])
   new_item.save()
   return HttpResponseRedirect('/todo/')

def deleteTodo (request, todo_id):
    itemtodelete = TodoItem.objects.get(id=todo_id)
    itemtodelete.delete()
    return HttpResponseRedirect('/todo/')