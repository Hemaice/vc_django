from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.template import loader
def vcregister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        return redirect('login')
    return render(request, 'vcregister.html')

def vclogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return redirect('vcgetstart.html')
        else:
            return render(request, 'vclogin.html', {'error': 'Invalid username or password'})
    return render(request, 'vclogin.html')

def vcgetstart(request):
    template = loader.get_template('vcgetstart.html')
    return HttpResponse(template.render())

def vccourse(request):
    template = loader.get_template('vccourse.html')
    return HttpResponse(template.render())

def vcassignmet(request):
    template = loader.get_template('vcassignmet.html')
    return HttpResponse(template.render())

def vcasssubmitted(request):
    template = loader.get_template('vcasssubmitted.html')
    return HttpResponse(template.render())

def vcuploadfile(request):
    template = loader.get_template('vcuploadfile.html')
    return HttpResponse(template.render())

def vchome(request):
    template = loader.get_template('vchome.html')
    return HttpResponse(template.render())