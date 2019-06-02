from django.shortcuts import render


from questionario import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def questionario(request):
    context = {'error': ''}
    return render(request,'questionario_user.html',context)
