# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0002_stats_1to1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='participating_team',
            field=models.OneToOneField(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
    ]
