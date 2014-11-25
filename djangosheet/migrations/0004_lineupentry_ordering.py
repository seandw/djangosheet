# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0003_lineup_1to1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineupentry',
            options={'verbose_name_plural': 'lineup entries', 'ordering': ['batting_position']},
        ),
    ]
