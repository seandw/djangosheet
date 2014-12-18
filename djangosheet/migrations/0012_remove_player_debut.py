# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0011_remove_1to1_model_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='debut',
        ),
    ]
