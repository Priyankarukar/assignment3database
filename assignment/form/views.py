from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from . models import Students

# Create your views here.
def form(request):
    f1=forms.MyForm()
    return render(request,"form.html",{'form':f1})
def index(request):
    data=Students.objects.all()
    return render(request,'index.html',{"studentdata":data})

def getdata(request):
    if request.method == "GET":
        un = request.GET['uname']
        ps = request.GET['Password']
        pn = request.GET['Pnumber']
        add = request.GET['Address']
        return render(request,"valid.html", {"username":un,"password": ps,"pnumber":pn,"address":add})

    if request.method == "POST":
        un = request.POST['uname']
        ps = request.POST['Password']
        pn = request.POST['Pnumber']
        add = request.POST['Address']
        s1=models.Students(uname=un,Password=ps,Pnumber=pn,Address=add)
        s1.save()
        return render(request,"valid.html", {"username":un,"password": ps, "pnumber": pn, "address": add})
