from django.shortcuts import render, redirect
from.models import Course
# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name = request.POST['user_name'], description = request.POST['user_description'])
    return redirect('/') 

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
