from django.shortcuts import render
from django.http import HttpResponse
from .models import rassavni_foundation


def index(request):
    bl=rassavni_foundation.objects.all()
    per={'bl':bl}
    return render(request, 'rass/index.html',per)
    