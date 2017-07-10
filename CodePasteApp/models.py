# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Code(models.Model):
    data = models.CharField(max_length=10000)
    link = models.CharField(max_length=5, blank=True, unique=True)
    title = models.CharField(max_length=20,blank=True)
    password = models.CharField(max_length=20,blank=True)

    def __unicode__(self):
        return self.data


