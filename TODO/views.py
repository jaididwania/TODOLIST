from django.shortcuts import render
from django.utils import timezone

def home(request):
    return render(request,'main/index.html')

def add_todo(request):
    
    added_date = timezone.now()
    content = request.POST['content']
    print(added_date)
    print(content)
    return render(request,'main/index.html')