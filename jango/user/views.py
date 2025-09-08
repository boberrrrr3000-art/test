from django.shortcuts import render
from django.http import HttpResponse
from .models import user

def index(request):
    name = user.objects.all()
    return render(request, 'user/users.html', {'name': name})
