# coding: utf-8
from django.db import models

# Create your models here.
class Sender(models.Model):
    name= models.CharField(max_length=20)
    ps = models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.BooleanField(default=True)
    title=models.CharField(max_length=20)
    contents = models.CharField(max_length=900)
    lasttime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return '%s'%(self.name)
