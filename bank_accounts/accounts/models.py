# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iban = models.CharField(max_length=34)
    creator = models.ForeignKey(User, related_name='accounts')
