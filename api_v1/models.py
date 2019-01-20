# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
1
class TestDataset(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(default="", max_length=500)

    def __str__(self):
        return str(self.id)