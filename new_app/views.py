from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request,'views.html')
def index(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dash.html')