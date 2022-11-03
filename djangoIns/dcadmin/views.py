from django.http import response, HttpResponse
from django.shortcuts import render, redirect
from .models import HostAdd, HostDevice, HostInsGroup
# Create your views here.

def login(request):
    return render(request, "index.html")
def info(request):
    hostlist = HostAdd.objects.values()
    # hostlist = HostAdd.objects.all()
    return render(request, "info.html", locals())
def add(request):
    return render(request, "hostadd.html")

def addhostdevice(request):
    if request.POST:
        device = request.POST['hostdevice']
        HostDevice.objects.create(device=device)
        return redirect("/user/device/")
    return render(request, "adddevice.html")

def device(request):
    device = HostDevice.objects.all()
    return render(request, "device.html", locals())


def addInsGroup(request):
    if request.POST:
        hostins = request.POST['hostins']
        HostInsGroup.objects.create(InsGroupName=hostins)
        return redirect("/user/insinfo/")
    return render(request, "addins.html")

def insinfo(request):
    insinfo = HostInsGroup.objects.all()
    return render(request, "insinfo.html", locals())

def hostAdd(request):
    if request.POST:
        hostip = request.POST['hostip']
        hostname = request.POST['hostname']
        hostusername = request.POST['hostusername']
        hostpassword = request.POST['hostpassword']
        hostport = request.POST['hostport']
        hostdevice = request.POST['device']
        hostinsgroup = request.POST['insGroup']
        hostsave = HostAdd.objects.create(hostip=hostip,
                           hostname=hostname,
                           hostusername=hostusername,
                           hostpassword=hostpassword,
                           hostport=hostport,
                           hostdevice=hostdevice,
                           hostinsGroup=hostinsgroup)
        return redirect("/user/info/")
    device_lsit = HostDevice.objects.all()
    insGroup_list = HostInsGroup.objects.all()
    return render(request, "hostadd.html", locals())

def hostDel(request,id):
    idinfo = HostAdd.objects.filter(id=id).first()
    idinfo.delete()
    return redirect("/user/info/")

def hostEdit(request,id):
    idinfo = HostAdd.objects.filter(id=id).first()
    if request.method == "POST":
        hostip = request.POST['hostip']
        hostname = request.POST['hostname']
        hostusername = request.POST['hostusername']
        hostpassword = request.POST['hostpassword']
        hostport = request.POST['hostport']
        hostdevice = request.POST['device']
        hostinsgroup = request.POST['insGroup']
        HostAdd.objects.filter(id=id).update(hostip=hostip,
                                             hostname=hostname,
                                             hostusername=hostusername,
                                             hostpassword=hostpassword,
                                             hostport=hostport,
                                             hostdevice=hostdevice,
                                             hostinsGroup=hostinsgroup)
        return redirect("/user/info/")
    device_lsit = HostDevice.objects.all()
    insGroup_list = HostInsGroup.objects.all()
    return render(request, "edit.html", locals())

def insHost(request):
    return HttpResponse("设备巡检")