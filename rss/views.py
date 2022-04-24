from django.shortcuts import render
from django.http import HttpResponse,request
from .models import rassav,aboutme,ProfessionalExperience,skill,cert,ed_qua,cop,events


def index(request):
    rs=rassav.objects.all()
    ab=aboutme.objects.all()
    pe=ProfessionalExperience.objects.all()
    sk=skill.objects.all()
    ce=cert.objects.all()
    ee=ed_qua.objects.all()
    co=cop.objects.all()
    params ={'rs':rs,'ab':ab,'pe':pe,'ee':ee,'co':co,'sk':sk,'ce':ce}
    return render(request,'rss/index.html',params)

def ser(request):
    return render(request,'rss/service.html')

def event(request):
    ev=events.objects.all()
    par={'ev':ev}
    return render(request,'rss/event.html',par)