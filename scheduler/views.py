from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from .models import Job


def schedule_chart(request):
    jobs = Job.objects.order_by('start').order_by('lineno')    
    return render(request, 'schedule_chart.html', {'jobs': jobs})


def schedule_table(request):
    jobs = Job.objects.order_by('start').order_by('lineno')    
    return render(request, 'schedule_table.html', {'jobs': jobs})
