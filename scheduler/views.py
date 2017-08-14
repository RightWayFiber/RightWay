from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from .models import Job


def chart(request):
    jobs = Job.objects.order_by('start').order_by('lineno')    
    return render(request, 'scheduler/chart.html', {'jobs': jobs})


def table(request):
    jobs = Job.objects.order_by('start').order_by('lineno')    
    return render(request, 'scheduler/table.html', {'jobs': jobs})
