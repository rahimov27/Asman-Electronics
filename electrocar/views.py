from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
# def index(request):
#     return render(request, 'base.html')

def addclient(request):
    if request.method == 'POST':
        form = ClientForms(request.POST)
        if form.is_valid():
            # client = Client.objects.create(**form.cleaned_data)
            form.save()
            return redirect('/')
    else:
        forms = ClientForms()
    return render(request, 'electrocar/base.html', {'form': forms})







    