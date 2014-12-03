# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_results(apps, schema_editor):
    Game = apps.get_model('djangosheet', 'Game')
    for game in Game.objects.all():
        winner, loser = game.participatingteam_set.all()[:]
        if loser.runs > winner.runs:
            winner, loser = loser, winner
        elif winner.runs == loser.runs:
            continue  # Nothing to save here, no winner or loser
        winner.result = 'W'
        winner.save()
        loser.result = 'L'
        loser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangosheet', '0006_participatingteam_result'),
    ]

    operations = [
        migrations.RunPython(add_results),
    ]
