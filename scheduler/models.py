from django.db import models
from django.utils import timezone


class Job(models.Model):
    author = models.ForeignKey('auth.User')
    lineno = models.CharField(max_length=32, default='')
    lotno = models.CharField(max_length=32, default='')
    colorname = models.CharField(max_length=32, default='')
    qty = models.PositiveIntegerField(default=0)
    start = models.DateTimeField(default=timezone.now)
    finish = models.DateTimeField(default=timezone.now)

    def register(self):        
        self.save()

    def __str__(self):
        return self.lotno
