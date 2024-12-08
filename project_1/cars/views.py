from django.shortcuts import render

# Create your views here.

def bmw(request):
    return render(request,'bmw.html')

def benz(request):
    return render(request,'benz.html')
