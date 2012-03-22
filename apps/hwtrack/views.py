# Create your views here.
from django.shortcuts import render_to_response as render
from django import forms

from forms import AddDeviceForm, ServiceCheckinForm
from hwtrack.models import Device, Computer
#from service.models import RenderDeviceService, SymptomInstance

from contact.forms import UserContactForm, UserProfileForm

def all_computers(request):
    devices = Computer.objects.order_by('id')
    return render('hwtrack/all_devices.html', locals())

def all_devices(request):
    devices = Device.objects.order_by('id')
    return render('hwtrack/all_devices.html', locals())


# Zack wrote this crap.
def displayDevice(request, device_id):
    device = Device.objects.get(id=device_id)
    return render('hwtrack/displayDevice.html', locals())



def Computer_Owner(request):
    from hwtrack.models import Computer
    computers = Computer.objects.all()
    return render('computer_owner.html', locals())