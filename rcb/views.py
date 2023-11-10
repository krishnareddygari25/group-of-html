from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'rcb.html')

def kohilli(request):
    return HttpResponse('<h1> best captain</h1>')