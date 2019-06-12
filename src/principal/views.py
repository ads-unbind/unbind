from django.shortcuts import render
from usuario import models


def index(request):
    return render(request, 'index.html')
