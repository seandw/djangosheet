# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0010_cleanup_current_franchise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defensivestats',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lineup',
            name='id',
        ),
        migrations.RemoveField(
            model_name='offensivestats',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pitchingstats',
            name='id',
        ),
        migrations.AlterField(
            model_name='defensivestats',
            name='participating_team',
            field=models.OneToOneField(serialize=False, to='djangosheet.ParticipatingTeam', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lineup',
            name='participating_team',
            field=models.OneToOneField(serialize=False, to='djangosheet.ParticipatingTeam', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offensivestats',
            name='participating_team',
            field=models.OneToOneField(serialize=False, to='djangosheet.ParticipatingTeam', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='participating_team',
            field=models.OneToOneField(serialize=False, to='djangosheet.ParticipatingTeam', primary_key=True),
            preserve_default=True,
        ),
    ]
