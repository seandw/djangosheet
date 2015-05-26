# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0012_remove_player_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerteam',
            name='year',
            field=models.IntegerField(),
        ),
    ]
