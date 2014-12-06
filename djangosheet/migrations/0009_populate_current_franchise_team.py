# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_current_teams(apps, schema_editor):
    Team = apps.get_model('djangosheet', 'Team')
    current_teams = {team.franchise: team for team in Team.objects.filter(end__isnull=True)}
    for team in Team.objects.all():
        team.current_franchise_team = current_teams[team.current_franchise]
        team.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0008_add_current_franchise_team'),
    ]

    operations = [
        migrations.RunPython(add_current_teams),
    ]
