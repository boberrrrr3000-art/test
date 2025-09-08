from django.shortcuts import render
from django.http import HttpResponse
from .models import impytADMIN
from .forms import impytADMINForm
# Create your views here.
def index(request):
        if  request.method == 'POST':     
            form = impytADMINForm(request.POST)
            form.save()
        form = impytADMINForm()
        impyt = impytADMIN.objects.all()
        return render(request, 'index.html', {'form': form, 'impyt': impyt})
