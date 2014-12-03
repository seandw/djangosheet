# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0004_lineupentry_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='losing_pitcher',
            field=models.ForeignKey(blank=True, null=True, to='djangosheet.Player', related_name='losing_pitcher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='winning_pitcher',
            field=models.ForeignKey(blank=True, null=True, to='djangosheet.Player', related_name='winning_pitcher'),
            preserve_default=True,
        ),
    ]
