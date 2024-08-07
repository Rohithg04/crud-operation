from django.shortcuts import render, redirect

from new_app.forms import WaterLand, Water_Land


# Create your views here.
def app(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def dash(request):
     return render(request,'dash.html')

def submit(request):
    form=Water_Land()
    if request.method == 'POST':
        data = Water_Land(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'submit.html',{'form':form})
def WaterLand_view(request):
    data = WaterLand.objects.all()
    return render(request,'view.data.html',{'data':data})
def WaterLand_delete(request,id):
    data = WaterLand.objects.get(id=id)
    data.delete()
    return redirect('WaterLand_view')
def WaterLand_update(request,id):
    data = WaterLand.objects.get(id=id)
    form = Water_Land(instance = data)
    if request.method == 'POST':
        data = Water_Land(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect("WaterLand_view")
    return render(request,'update.html',{'form':form})