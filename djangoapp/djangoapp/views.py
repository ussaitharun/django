from django.shortcuts import render
from django.http import HttpResponse

def tharun(request):
    
    return render(request,'usst.html')

def subm(request):
    return render(request,'ans.html')
   