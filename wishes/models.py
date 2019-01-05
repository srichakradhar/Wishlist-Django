# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Wish(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='')
    wishtext = models.TextField()

    class Meta:
        ordering = ('created',)
