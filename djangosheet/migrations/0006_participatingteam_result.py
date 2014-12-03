# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0005_blank_pitcher_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatingteam',
            name='result',
            field=models.CharField(max_length=1, blank=True, choices=[('W', 'Win'), ('L', 'Loss')], null=True),
            preserve_default=True,
        ),
    ]
