from django.shortcuts import render
from django.utils import timezone
from TODO.models import TODO
from django.http import HttpResponseRedirect

def home(request):
    #grabbing todo items from database
    todo_items = TODO.objects.all().order_by("-added_date")
    context = {
        "todo_items": todo_items
    }
    return render(request,'main/index.html', context)

def add_todo(request):
    
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = TODO.objects.create(added_date = current_date,text= content)

    return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
    print(todo_id)
    return HttpResponseRedirect("/")
