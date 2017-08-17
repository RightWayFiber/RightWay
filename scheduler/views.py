from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from .models import Job

from collections import defaultdict
from pytz import timezone


def chart(request):
    tz = timezone('Asia/Seoul')
    jobs = Job.objects.order_by('start').order_by('lineno')
    job_dict = defaultdict(lambda: [])
    for job in jobs:
        job_dict[job.lineno].append(job)
    linenos = job_dict.keys()
    linenos = sorted(linenos)
    height = len(linenos) * 150
    data = []
    for lineno in linenos:
        item = {'category': lineno, 'segments': []}
        jobs = job_dict[lineno]
        for job in jobs:            
            segment = {
                'lotno': job.lotno,
                "colorname": job.colorname,
                "qty": job.qty,
                "start": job.start.astimezone(tz).strftime('%Y-%m-%d-%H'),
                "end": job.finish.astimezone(tz).strftime('%Y-%m-%d-%H')
            }
            item['segments'].append(segment)
        data.append(item)        

    return render(request, 'scheduler/chart.html', {'chart_data': data, 'chart_height': height})


def table(request):
    jobs = Job.objects.order_by('start').order_by('lineno')    
    return render(request, 'scheduler/table.html', {'jobs': jobs})
