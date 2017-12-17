# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect, reverse

from .forms import AccountForm
from .models import Account


def staff_required(func):
    """
    There should be staff permissions to manage accounts
    """
    def check_perms(user):
        if user.is_staff:
            return True
        raise PermissionDenied
    return user_passes_test(check_perms)(func)


@login_required
def list_accounts(request):
    if not request.user.is_staff:
        return render(request, 'accounts/no-permissions.html')
    accounts = Account.objects.filter(creator=request.user)
    return render(request, 'accounts/list.html', {'accounts': accounts})


@login_required
@staff_required
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
@staff_required
def view_account(request, pk):
    account = get_object_or_404(Account, pk=pk, creator=request.user)

    return render(request, 'accounts/view.html', {'account': account})


@login_required
@staff_required
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
@staff_required
def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk, creator=request.user)

    if request.method == 'POST':
        # Account will be cascade deleted
        User.objects.filter(pk=account.user.id).delete()
        return redirect(reverse('list-accounts'))

    return render(request, 'accounts/delete.html', {'account': account})
