# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, reverse

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
            data = form.cleaned_data

            user = User.objects.create_user(
                username=uuid.uuid4().hex,
                first_name=data['first_name'],
                last_name=data['last_name']
            )

            account = Account()
            account.user = user
            account.iban = data['iban']
            account.creator = request.user
            account.save()

            return redirect(reverse('list-accounts'))

    return render(request, 'accounts/create.html', {'form': form})


@login_required
def view_account(request, pk):
    account = get_object_or_404(Account, pk=pk, creator=request.user)

    return render(request, 'accounts/view.html', {'account': account})


@login_required
def update_account(request, pk):
    account = get_object_or_404(Account, pk=pk, creator=request.user)

    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data

            account.user.first_name=data['first_name']
            account.user.last_name=data['last_name']
            account.user.save(update_fields=['first_name', 'last_name'])

            account.iban=data['iban']
            account.save(update_fields=['iban'])

            return redirect(reverse('list-accounts'))
    else:
        form = AccountForm(initial={
            'first_name': account.user.first_name,
            'last_name': account.user.last_name,
            'iban': account.iban,
        })

    return render(request, 'accounts/update.html', {
        'form': form,
        'account': account,
    })


@login_required
def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk, creator=request.user)

    if request.method == 'POST':
        # Account will be cascade deleted
        User.objects.filter(pk=account.user.id).delete()
        return redirect(reverse('list-accounts'))

    return render(request, 'accounts/delete.html', {'account': account})
