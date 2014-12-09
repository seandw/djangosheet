import csv
import glob
import re
import os

from django.core.management.base import LabelCommand, CommandError
from django.db import transaction
from djangosheet.models import Team, Park, Player, PlayerTeam, Game, ParticipatingTeam, Lineup, \
    LineupEntry, OffensiveStats, DefensiveStats, PitchingStats


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
PARKS = 'parks.csv'
TEAMS = 'teams.csv'
PEOPLE = 'people.csv'
ROSTER_MASK = '*{0}.ROS'
GAMES_MASK = 'games-{0}.csv'


class Command(LabelCommand):
    args = '<year year ...>'
    help = 'Loads Retrosheet data for the specified years into the database'

    def handle_label(self, year, **options):
        if Team.objects.count() == 0:
            self.stderr.write('No teams in database, must add them first.')
            self.load_teams()
        if Park.objects.count() == 0:
            self.stderr.write('No parks in database, must add them first.')
            self.load_parks()
        if Player.objects.count() == 0:
            self.stderr.write('No people in database, must add them first.')
            self.load_people()

        self.stdout.write('Processing year {0}...'.format(year))
        self.load_players(year)
        self.load_games(year)

    @transaction.atomic
    def load_teams(self):
        self.stdout.write('Adding teams to database...')

        current_franchises = dict()
        with open(os.path.join(DATA_DIR, TEAMS)) as teams_file:
            cols = ['current_franchise', 'franchise', 'league', 'division', 'location', 'name',
                    'nicknames', 'start', 'end', 'city', 'state']
            reader = csv.DictReader(teams_file, fieldnames=cols)
            for row in reader:
                month, day, year = re.findall(r'\d+', row['start'])
                row['start'] = year + '-' + month + '-' + day
                if row['end'] != '':
                    month, day, year = re.findall(r'\d+', row['end'])
                    row['end'] = year + '-' + month + '-' + day
                else:
                    del row['end']
                current_franchises.setdefault(row['current_franchise'], set()).add(row['franchise'])
                del row['current_franchise']
                Team(**row).save()

        current_teams = dict()
        for team in Team.objects.filter(end__isnull=True):
            for franchise in current_franchises[team.franchise]:
                current_teams[franchise] = team
        for team in Team.objects.all():
            team.current_franchise = current_teams[team.franchise]
            team.save()

    @transaction.atomic
    def load_parks(self):
        self.stdout.write('Adding parks to database...')
        with open(os.path.join(DATA_DIR, PARKS)) as parks_file:
            reader = csv.DictReader(parks_file)
            for row in reader:
                month, day, year = re.findall(r'\d+', row['start'])
                row['start'] = year + '-' + month + '-' + day
                if row['end'] != '':
                    month, day, year = re.findall(r'\d+', row['end'])
                    row['end'] = year + '-' + month + '-' + day
                else:
                    del row['end']
                Park(**row).save()

    @transaction.atomic
    def load_people(self):
        self.stdout.write('Adding people to database...')
        with open(os.path.join(DATA_DIR, PEOPLE)) as people_file:
            # File includes umpires, managers. At some point, this should be differentiated.
            reader = csv.DictReader(people_file)
            for row in reader:
                month, day, year = re.findall(r'\d+', row['debut'])
                row['debut'] = year + '-' + month + '-' + day
                Player(**row).save()

    @transaction.atomic
    def load_players(self, year):
        self.stdout.write('Processing players...')
        cols = ['id', 'last_name', 'first_name', 'batting_hand', 'throwing_hand', 'team',
                'position']
        teams = Team.get_by_year(year)
        path = os.path.join(DATA_DIR, ROSTER_MASK.format(year))
        files = glob.glob(path)
        if len(files) == 0:
            raise CommandError('No roster data for the year {0}. '.format(year) +
                               'You must first download it with retro_dl')
        for roster in files:
            with open(roster) as roster_file:
                reader = csv.DictReader(roster_file, fieldnames=cols)
                for player_dict in reader:
                    PlayerTeam.objects.update_or_create(year=year, player_id=player_dict['id'],
                                                        team=teams.get(franchise=player_dict['team']),
                                                        defaults={'position': player_dict['position'],
                                                                  'batting_hand': player_dict['batting_hand'],
                                                                  'throwing_hand': player_dict['throwing_hand']})

    @transaction.atomic
    def load_games(self, year):
        self.stdout.write('Processing games...')
        cols = ['id', 'date', 'day_of_week', 'start', 'time_of_day', 'away_team', 'home_team',
                'park_id', 'away_starting_pitcher_id', 'home_starting_pitcher_id', 'attendance',
                'temperature', 'wind_direction', 'wind_speed', 'field_condition', 'precipitation',
                'sky', 'time', 'innings', 'away_runs', 'home_runs', 'away_hits', 'home_hits',
                'away_errors', 'home_errors', 'away_left_on_base', 'home_left_on_base',
                'winning_pitcher_id', 'losing_pitcher_id', 'save_pitcher_id', 'away_lineup_1',
                'away_lineup_1_pos', 'away_lineup_2', 'away_lineup_2_pos', 'away_lineup_3',
                'away_lineup_3_pos', 'away_lineup_4', 'away_lineup_4_pos', 'away_lineup_5',
                'away_lineup_5_pos', 'away_lineup_6', 'away_lineup_6_pos', 'away_lineup_7',
                'away_lineup_7_pos', 'away_lineup_8', 'away_lineup_8_pos', 'away_lineup_9',
                'away_lineup_9_pos', 'home_lineup_1', 'home_lineup_1_pos', 'home_lineup_2',
                'home_lineup_2_pos', 'home_lineup_3', 'home_lineup_3_pos', 'home_lineup_4',
                'home_lineup_4_pos', 'home_lineup_5', 'home_lineup_5_pos', 'home_lineup_6',
                'home_lineup_6_pos', 'home_lineup_7', 'home_lineup_7_pos', 'home_lineup_8',
                'home_lineup_8_pos', 'home_lineup_9', 'home_lineup_9_pos', 'away_last_pitcher_id',
                'home_last_pitcher_id', 'outs', 'completion_info', 'forfeit_info', 'protest_info',
                'away_line', 'home_line', 'away_os_at_bats', 'away_os_doubles', 'away_os_triples',
                'away_os_home_runs', 'away_os_rbis', 'away_os_sac_hits', 'away_os_sac_flies',
                'away_os_hbps', 'away_os_walks', 'away_os_ibbs', 'away_os_strikeouts',
                'away_os_stolen_bases', 'away_os_caught_stealing', 'away_os_gidps',
                'away_os_reached_on_interference', 'away_ps_pitchers', 'away_ps_earned_runs',
                'away_ps_team_earned_runs', 'away_ps_wild_pitches', 'away_ps_balks',
                'away_ds_putouts', 'away_ds_assists', 'away_ds_passed_balls',
                'away_ds_double_plays', 'away_ds_triple_plays', 'home_os_at_bats',
                'home_os_doubles', 'home_os_triples', 'home_os_home_runs', 'home_os_rbis',
                'home_os_sac_hits', 'home_os_sac_flies', 'home_os_hbps', 'home_os_walks',
                'home_os_ibbs', 'home_os_strikeouts', 'home_os_stolen_bases',
                'home_os_caught_stealing', 'home_os_gidps', 'home_os_reached_on_interference',
                'home_ps_pitchers', 'home_ps_earned_runs', 'home_ps_team_earned_runs',
                'home_ps_wild_pitches', 'home_ps_balks', 'home_ds_putouts', 'home_ds_assists',
                'home_ds_passed_balls', 'home_ds_double_plays', 'home_ds_triple_plays']
        ha_pattern = re.compile('(home|away)_')
        path = os.path.join(DATA_DIR, GAMES_MASK.format(year))
        if not os.path.isfile(path):
            raise CommandError('No games data for the year {0}. '.format(year) +
                               'You must first process it with retro_process')
        with open(path) as games_file:
            reader = csv.DictReader(games_file, fieldnames=cols)
            for game in reader:
                game_id = game['id']
                del game['id']
                date = game['date']
                game['date'] = date[:4] + '-' + date[4:6] + '-' + date[6:]
                # Ties, complete games, or games without saves have invalid IDs in these fields
                for possible_empty_id in ['save_pitcher_id', 'winning_pitcher_id',
                                          'losing_pitcher_id', 'away_last_pitcher_id',
                                          'home_last_pitcher_id']:
                    if game[possible_empty_id] == '':
                        del game[possible_empty_id]
                if int(game['home_runs']) > int(game['away_runs']):
                    game['home_result'] = 'W'
                    game['away_result'] = 'L'
                elif int(game['home_runs']) < int(game['away_runs']):
                    game['home_result'] = 'L'
                    game['away_result'] = 'W'
                game_info = {key: value for key, value in game.items()
                             if not ha_pattern.match(key)}
                game_object, _ = Game.objects.update_or_create(id=game_id, defaults=game_info)
                self.generate_team_stats(game_object, game, 'home_')
                self.generate_team_stats(game_object, game, 'away_')


    @staticmethod
    def generate_team_stats(game_object, game_dict, prefix):
        game_info = {key[5:]: value for key, value in game_dict.items() if key.startswith(prefix)}
        pt_pattern = re.compile('([dop]s|lineup)_')
        pt_info = {key: value for key, value in game_info.items() if not pt_pattern.match(key)}
        pt_info['team'] = Team.get_by_year(game_dict['date'][:4]).get(franchise=pt_info['team'])
        pt_info['side'] = 'H' if prefix == 'home_' else 'A'
        pt, _ = ParticipatingTeam.objects.update_or_create(game=game_object, defaults=pt_info)

        lineup, created = Lineup.objects.get_or_create(participating_team=pt,
                                                       defaults={'team': pt_info['team'],
                                                                 'date': game_dict['date']})
        if not created:
            LineupEntry.objects.filter(lineup=lineup).delete()

        for position in range(1, 10):
            key = 'lineup_{0}'.format(position)
            LineupEntry(lineup=lineup, player_id=game_info[key], batting_position=position,
                        defensive_position=game_info[key + '_pos']).save()

        OffensiveStats.objects.update_or_create(participating_team=pt,
                                                defaults={key[3:]: value
                                                          for key, value in game_info.items()
                                                          if key.startswith('os_')})
        DefensiveStats.objects.update_or_create(participating_team=pt,
                                                defaults={key[3:]: value
                                                          for key, value in game_info.items()
                                                          if key.startswith('ds_')})
        PitchingStats.objects.update_or_create(participating_team=pt,
                                               defaults={key[3:]: value
                                                         for key, value in game_info.items()
                                                         if key.startswith('ps_')})
