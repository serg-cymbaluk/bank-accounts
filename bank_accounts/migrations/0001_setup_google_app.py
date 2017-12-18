# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


def setup_google_app(apps, schema_editor):
    SocialApp = apps.get_model('socialaccount', 'SocialApp')
    Site = apps.get_model('sites', 'Site')

    # This migration has only test purpose.
    # In a real application security keys should be setted up manualy
    # or by means of some external tools.
    social_app = SocialApp.objects.create(
        provider='google',
        name='bank-accounts',
        client_id='502452262639-7s12tni361ag99cmcoastiqn8n0a22ia.apps.googleusercontent.com',
        secret='GomlnLPvaM0cqNlkPXJ9RnYV'
    )

    site, created = Site.objects.get_or_create(
        name='localhost:8000',
        domain='localhost:8000'
    )

    social_app.sites.add(site)


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.RunPython(setup_google_app)
    ]
