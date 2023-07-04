from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic_add(request):
    if request.method == 'POST':
        TO=request.POST.get('topic_name')
        XO=Topic.objects.get_or_create(Topic_name=TO)
        return HttpResponse('Topic added successfully!!!')
    return render(request,'topic_add.html')

def web_add(request):
    WO = Topic.objects.all()
    context={'WO':WO}
    if request.method=='POST':
        WO1=request.POST['tn']
        WO2=Topic.objects.get(Topic_name=WO1)
        XO=request.POST['na']
        NO=request.POST['ur']
        XNO=Webpage.objects.get_or_create(Topic_name=WO2,Name=XO,Url=NO)[0]
        XNO.save()
        return HttpResponse('WEBPAGES ADDED SUCCESSSFULLY!!!!!')
    return render(request,'web_add.html',context)

        
def retrive(request):
    WP=Topic.objects.all()
    d={'WP': WP}
    if request.method=='POST':
        WSTS=request.POST.getlist('tn')
        EQS=Webpage.objects.none()
        for i in WSTS:
            EQS = EQS | Webpage.objects.filter(Topic_name=i)
        d1={'EQS' : EQS }
        return render(request,'display.html',d1)
    return render(request,'retrive.html',d)
    

