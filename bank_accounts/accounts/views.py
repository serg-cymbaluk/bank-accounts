# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse

from .forms import AccountForm
from .models import Account


@login_required
def list_accounts(request):
    accounts = Account.objects.filter(creator=request.user)
    return render(request, 'accounts/list.html', {'accounts': accounts})


@login_required
def create_account(request):
    form = AccountForm()

    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=uuid.uuid4().hex,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            account = Account.objects.create(
                user=user,
                iban=form.cleaned_data['iban'],
                creator=request.user
            )
            return redirect(reverse('list-accounts'))

    return render(request, 'accounts/create.html', {'form': form})


@login_required
def view_account(request, pk):
    return render(request, 'accounts/view.html')


@login_required
def update_account(request, pk):
    return render(request, 'accounts/update.html')


@login_required
def delete_account(request, pk):
    return render(request, 'accounts/delete.html')
