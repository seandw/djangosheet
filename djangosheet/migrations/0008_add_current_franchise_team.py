# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0007_add_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='current_franchise_team',
            field=models.ForeignKey(to='djangosheet.Team', null=True),
            preserve_default=True,
        ),
    ]
