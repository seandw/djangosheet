# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defensivestats',
            name='participating_team',
            field=models.OneToOneField(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offensivestats',
            name='participating_team',
            field=models.OneToOneField(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='participating_team',
            field=models.OneToOneField(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
    ]
