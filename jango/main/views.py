from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import impytADMIN
from .forms import impytADMINForm
# Create your views here.
def index(request):
        if  request.method == 'POST':     
            form = impytADMINForm(request.POST)
            if form.is_valid():
                form.save()
                #return redirect('main')
            else:
                form = impytADMINForm()
        impyt = impytADMIN.objects.all()
        return render(request, 'index.html', {'form': form, 'impyt': impyt})
