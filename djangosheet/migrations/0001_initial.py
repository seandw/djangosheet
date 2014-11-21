# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefensiveStats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('putouts', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('passed_balls', models.IntegerField()),
                ('double_plays', models.IntegerField()),
                ('triple_plays', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'defensive stats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('day_of_week', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=9)),
                ('start', models.IntegerField()),
                ('time_of_day', models.CharField(choices=[('D', 'Day'), ('N', 'Night')], max_length=1)),
                ('attendance', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('wind_direction', models.IntegerField(choices=[(0, 'Unknown'), (1, 'To LF'), (2, 'To CF'), (3, 'To RF'), (4, 'LF to RF'), (5, 'From LF'), (6, 'From CF'), (7, 'From RF'), (8, 'RF to LF')])),
                ('wind_speed', models.IntegerField()),
                ('field_condition', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Soaked'), (2, 'Wet'), (3, 'Damp'), (4, 'Dry')])),
                ('precipitation', models.IntegerField(choices=[(0, 'Unknown'), (1, 'None'), (2, 'Drizzle'), (3, 'Showers'), (4, 'Rain'), (5, 'Snow')])),
                ('sky', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Sunny'), (2, 'Cloudy'), (3, 'Overcast'), (4, 'Night'), (5, 'Dome')])),
                ('time', models.IntegerField()),
                ('innings', models.IntegerField()),
                ('outs', models.IntegerField()),
                ('completion_info', models.TextField(blank=True)),
                ('forfeit_info', models.TextField(blank=True)),
                ('protest_info', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineupEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('batting_position', models.IntegerField()),
                ('defensive_position', models.IntegerField(choices=[(1, 'Pitcher'), (2, 'Catcher'), (3, 'First baseman'), (4, 'Second baseman'), (5, 'Third baseman'), (6, 'Shortstop'), (7, 'Left fielder'), (8, 'Center fielder'), (9, 'Right fielder'), (10, 'Designated hitter')])),
                ('lineup', models.ForeignKey(to='djangosheet.Lineup')),
            ],
            options={
                'verbose_name_plural': 'lineup entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OffensiveStats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('at_bats', models.IntegerField()),
                ('doubles', models.IntegerField()),
                ('triples', models.IntegerField()),
                ('home_runs', models.IntegerField()),
                ('rbis', models.IntegerField()),
                ('sac_hits', models.IntegerField()),
                ('sac_flies', models.IntegerField()),
                ('hbps', models.IntegerField()),
                ('walks', models.IntegerField()),
                ('ibbs', models.IntegerField()),
                ('strikeouts', models.IntegerField()),
                ('stolen_bases', models.IntegerField()),
                ('caught_stealing', models.IntegerField()),
                ('gidps', models.IntegerField()),
                ('reached_on_interference', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'offensive stats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('aka', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('league', models.CharField(choices=[('NA', 'National Association'), ('NL', 'National League'), ('AA', 'American Association'), ('UA', 'Union Association'), ('PL', 'Players League'), ('AL', 'American League'), ('FL', 'Federal League')], max_length=2)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipatingTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('side', models.CharField(choices=[('H', 'Home'), ('A', 'Away')], max_length=1)),
                ('runs', models.IntegerField()),
                ('hits', models.IntegerField()),
                ('errors', models.IntegerField()),
                ('left_on_base', models.IntegerField()),
                ('line', models.TextField()),
                ('game', models.ForeignKey(to='djangosheet.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PitchingStats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pitchers', models.IntegerField()),
                ('earned_runs', models.IntegerField()),
                ('team_earned_runs', models.IntegerField()),
                ('wild_pitches', models.IntegerField()),
                ('balks', models.IntegerField()),
                ('participating_team', models.ForeignKey(to='djangosheet.ParticipatingTeam')),
            ],
            options={
                'verbose_name_plural': 'pitching stats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=8)),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('debut', models.DateField()),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('year', models.IntegerField(max_length=4)),
                ('position', models.CharField(choices=[('P', 'Pitcher'), ('C', 'Catcher'), ('1B', 'First baseman'), ('2B', 'Second baseman'), ('3B', 'Third baseman'), ('SS', 'Shortstop'), ('IF', 'Infielder'), ('LF', 'Left fielder'), ('CF', 'Center fielder'), ('RF', 'Right fielder'), ('OF', 'Outfielder'), ('DH', 'Designated hitter')], max_length=2)),
                ('batting_hand', models.CharField(choices=[('R', 'Right-handed'), ('L', 'Left-handed'), ('B', 'Switch hitter')], max_length=1)),
                ('throwing_hand', models.CharField(choices=[('R', 'Right-handed'), ('L', 'Left-handed')], max_length=1)),
                ('player', models.ForeignKey(to='djangosheet.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('current_franchise', models.CharField(max_length=3)),
                ('franchise', models.CharField(max_length=3)),
                ('league', models.CharField(choices=[('NA', 'National Association'), ('NL', 'National League'), ('AA', 'American Association'), ('AL', 'American League')], max_length=2)),
                ('division', models.CharField(choices=[('W', 'West'), ('C', 'Central'), ('E', 'East')], max_length=1, blank=True)),
                ('location', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('nicknames', models.CharField(max_length=255, blank=True)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playerteam',
            name='team',
            field=models.ForeignKey(to='djangosheet.Team'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='playerteam',
            unique_together=set([('player', 'year', 'team')]),
        ),
        migrations.AddField(
            model_name='participatingteam',
            name='last_pitcher',
            field=models.ForeignKey(related_name='last_pitcher', to='djangosheet.Player', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participatingteam',
            name='starting_pitcher',
            field=models.ForeignKey(related_name='starting_pitcher', to='djangosheet.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participatingteam',
            name='team',
            field=models.ForeignKey(to='djangosheet.Team'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='participatingteam',
            unique_together=set([('game', 'team')]),
        ),
        migrations.AddField(
            model_name='offensivestats',
            name='participating_team',
            field=models.ForeignKey(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineupentry',
            name='player',
            field=models.ForeignKey(to='djangosheet.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineup',
            name='participating_team',
            field=models.ForeignKey(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineup',
            name='team',
            field=models.ForeignKey(to='djangosheet.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='losing_pitcher',
            field=models.ForeignKey(related_name='losing_pitcher', to='djangosheet.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='park',
            field=models.ForeignKey(to='djangosheet.Park'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='save_pitcher',
            field=models.ForeignKey(related_name='save_pitcher', to='djangosheet.Player', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='winning_pitcher',
            field=models.ForeignKey(related_name='winning_pitcher', to='djangosheet.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defensivestats',
            name='participating_team',
            field=models.ForeignKey(to='djangosheet.ParticipatingTeam'),
            preserve_default=True,
        ),
    ]
