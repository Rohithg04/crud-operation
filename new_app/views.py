from django.shortcuts import render

from new_app.forms import WaterLand


# Create your views here.
def app(request):
    return render(request,'views.html')
def index(request):
    return render(request,'index.html')
def dash(request):
     return render(request,'dash.html')

def submit(request):
    form=WaterLand
    return render(request,'submit.html',{'form':form})