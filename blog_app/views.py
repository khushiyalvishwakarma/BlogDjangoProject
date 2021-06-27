from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import bloglist_form
from .models import bloglistmdl
# Create your views here.



def homefun(request):
    return render(request,'home.html')

def blogfun(request):
    ob=bloglist_form()
    return render(request,'addblog.html',{'form':ob})

def insert_blog(request):
    if request.method=="POST":
        ob = bloglist_form(request.POST)
        if ob.is_valid():
            ob.save()
            return redirect('/')


def display_blog(request):
    data=bloglistmdl.objects.all()
    return render(request,'display.html',{'data':data})


def editblog(request,id):
    records=bloglistmdl.objects.get(id=id)
    return render(request,'update.html',{'data':records})


def update_fun(request,id):
    if request.method=="POST":
        listrecord=bloglistmdl.objects.get(id=id)
        ob = bloglist_form(request.POST,instance=listrecord)
        if ob.is_valid():
            ob.save()
            return redirect('/displayblog')
    return render(request,'update.html',{'data':listrecord})


def delete_fun(request,id):
    blglist=bloglistmdl.objects.get(id=id)
    blglist.delete()
    return redirect('/displayblog')


def search(request):
    query = request.GET['query']
    data = bloglistmdl.objects.filter(title__icontains=query)
    params = {'data': data}
    return render(request,'show.html', params)

