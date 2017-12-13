# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def list_accounts(request):
    return render(request, 'accounts/list.html')
