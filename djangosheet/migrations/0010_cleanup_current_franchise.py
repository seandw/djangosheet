# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0009_populate_current_franchise_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='current_franchise',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='current_franchise_team',
            new_name='current_franchise',
        ),
    ]
