from django.shortcuts import render,HttpResponseRedirect
from .forms import studentform
from .models import students
# Create your views here.

def addandshow(request):
    if request.method =='POST':
        fm=studentform(request.POST)
        fm.save()
        fm=studentform()
    else:
        fm=studentform()
    stud=students.objects.all()
    return render(request, 'crud/addandshow.html',{'stud':stud, 'fm':fm})

def update(request,id):
    if request.method == 'POST':
        pi=students.objects.get(pk=id)
        fm=studentform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=students.objects.get(pk=id)
        fm=studentform(instance=pi)
    return render(request, 'crud/update.html',{'fm':fm})

def deletepost(request,id):
    if request.method == 'POST':
        fm=students.objects.get(pk=id)
        fm.delete()
    return HttpResponseRedirect('/')