from django.conf.urls import url

import bank_accounts.accounts.views as views

urlpatterns = [
    url(r'^list/$', views.list_accounts, name='list-accounts'),
    url(r'^create/$', views.create_account, name='create-account'),
    url(r'^view/(?P<pk>\d+)/$', views.view_account, name='view-account'),
    url(r'^update/(?P<pk>\d+)/$', views.update_account, name='update-account'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_account, name='delete-account'),
]
