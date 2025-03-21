from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def reg(request):
    form=regForm()
    if request.method=='POST':
        form=regForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request,'reg.html',{"form":form})
    form=regForm()
    return render(request,'task.html',{"form":form})



def details(request):
    data=Regmodel.objects.all()
    return render(request,'details.html',{"data":data})


def specific_detail(request,id):
    specific=Regmodel.objects.get(id=id)
    return render(request,'specific.html',{'specific':specific})


def update(request,id):
    update_task=Regmodel.objects.get(id=id)
    if request.method == 'POST': 
        form = regForm(request.POST, instance=update_task) 
        if form.is_valid(): 
            form.save() 
            return redirect('details')
    else: 
            form = regForm(instance=update_task)
    return render(request, 'update.html', {'form': form})

def delete(request,id):
    delete_task=Regmodel.objects.get(id=id)
    delete_task.delete()
    return redirect('details')