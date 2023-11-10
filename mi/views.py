from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'mi.html')
def bomraa(request):
    return HttpResponse('<h1> best captain</h1>')
