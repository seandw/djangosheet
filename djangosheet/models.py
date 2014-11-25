from django.db import models


class Team(models.Model):
    LEAGUES = (
        ('NA', 'National Association'),
        ('NL', 'National League'),
        ('AA', 'American Association'),
        ('AL', 'American League'),
    )
    DIVISIONS = (
        ('W', 'West'),
        ('C', 'Central'),
        ('E', 'East'),
    )

    current_franchise = models.CharField(max_length=3)
    franchise = models.CharField(max_length=3)
    league = models.CharField(max_length=2, choices=LEAGUES)
    division = models.CharField(max_length=1, blank=True, choices=DIVISIONS)
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nicknames = models.CharField(max_length=255, blank=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.location + ' ' + self.name

    @classmethod
    def get_by_year(cls, year):
        # magic specific date, all teams appear to start before May 20th
        start_date = year + '-5-20'
        return cls.objects.filter(models.Q(end__gte=start_date) | models.Q(end__isnull=True),
                                  start__lte=start_date)


class Park(models.Model):
    LEAGUES = (
        ('NA', 'National Association'),
        ('NL', 'National League'),
        ('AA', 'American Association'),
        ('UA', 'Union Association'),
        ('PL', 'Players League'),
        ('AL', 'American League'),
        ('FL', 'Federal League')
    )

    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=255)
    aka = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    league = models.CharField(max_length=2, choices=LEAGUES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name + ', ' + self.city + ', ' + self.state


class Player(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    debut = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['last_name', 'first_name']


class PlayerTeam(models.Model):
    POSITIONS = (
        ('P', 'Pitcher'),
        ('C', 'Catcher'),
        ('1B', 'First baseman'),
        ('2B', 'Second baseman'),
        ('3B', 'Third baseman'),
        ('SS', 'Shortstop'),
        ('IF', 'Infielder'),
        ('LF', 'Left fielder'),
        ('CF', 'Center fielder'),
        ('RF', 'Right fielder'),
        ('OF', 'Outfielder'),
        ('DH', 'Designated hitter'),
    )
    BATTING_HANDEDNESS = (
        ('R', 'Right-handed'),
        ('L', 'Left-handed'),
        ('B', 'Switch hitter'),
    )
    THROWING_HANDEDNESS = (
        ('R', 'Right-handed'),
        ('L', 'Left-handed'),
    )

    player = models.ForeignKey(Player)
    year = models.IntegerField(max_length=4)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length=2, choices=POSITIONS)
    batting_hand = models.CharField(max_length=1, choices=BATTING_HANDEDNESS)
    throwing_hand = models.CharField(max_length=1, choices=THROWING_HANDEDNESS)

    class Meta:
        unique_together = (('player', 'year', 'team'),)


class Game(models.Model):
    DAYS_OF_WEEK = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    TIMES_OF_DAY = (
        ('D', 'Day'),
        ('N', 'Night'),
    )
    WIND_DIRECTIONS = (
        (0, 'Unknown'),
        (1, 'To LF'),
        (2, 'To CF'),
        (3, 'To RF'),
        (4, 'LF to RF'),
        (5, 'From LF'),
        (6, 'From CF'),
        (7, 'From RF'),
        (8, 'RF to LF'),
    )
    FIELD_CONDITIONS = (
        (0, 'Unknown'),
        (1, 'Soaked'),
        (2, 'Wet'),
        (3, 'Damp'),
        (4, 'Dry'),
    )
    PRECIPITATION = (
        (0, 'Unknown'),
        (1, 'None'),
        (2, 'Drizzle'),
        (3, 'Showers'),
        (4, 'Rain'),
        (5, 'Snow'),
    )
    SKY = (
        (0, 'Unknown'),
        (1, 'Sunny'),
        (2, 'Cloudy'),
        (3, 'Overcast'),
        (4, 'Night'),
        (5, 'Dome'),
    )

    id = models.TextField(primary_key=True)
    date = models.DateField()
    day_of_week = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    start = models.IntegerField()
    time_of_day = models.CharField(max_length=1, choices=TIMES_OF_DAY)
    park = models.ForeignKey(Park)
    attendance = models.IntegerField()
    temperature = models.IntegerField()
    wind_direction = models.IntegerField(choices=WIND_DIRECTIONS)
    wind_speed = models.IntegerField()
    field_condition = models.IntegerField(choices=FIELD_CONDITIONS)
    precipitation = models.IntegerField(choices=PRECIPITATION)
    sky = models.IntegerField(choices=SKY)
    time = models.IntegerField()
    innings = models.IntegerField()
    winning_pitcher = models.ForeignKey(Player, related_name='winning_pitcher')
    losing_pitcher = models.ForeignKey(Player, related_name='losing_pitcher')
    save_pitcher = models.ForeignKey(Player, blank=True, null=True, related_name='save_pitcher')
    outs = models.IntegerField()
    completion_info = models.TextField(blank=True)
    forfeit_info = models.TextField(blank=True)
    protest_info = models.TextField(blank=True)

    @property
    def home(self):
        return self.participatingteam_set.get(side='H')

    @property
    def away(self):
        return self.participatingteam_set.get(side='A')

    def ordered_teams(self):
        return self.participatingteam_set.order_by('side')


class ParticipatingTeam(models.Model):
    SIDES = (
        ('H', 'Home'),
        ('A', 'Away'),
    )

    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    side = models.CharField(max_length=1, choices=SIDES)
    starting_pitcher = models.ForeignKey(Player, related_name='starting_pitcher')
    last_pitcher = models.ForeignKey(Player, blank=True, null=True, related_name='last_pitcher')

    runs = models.IntegerField()
    hits = models.IntegerField()
    errors = models.IntegerField()
    left_on_base = models.IntegerField()
    line = models.TextField()

    def line_as_list(self):
        import re
        return re.findall(r'((?<=\()\d+(?=\))|\d|x)', self.line)

    class Meta:
        unique_together = (('game', 'team'),)


class Lineup(models.Model):
    participating_team = models.OneToOneField(ParticipatingTeam)
    team = models.ForeignKey(Team)
    date = models.DateField()


class LineupEntry(models.Model):
    POSITIONS = (
        (1, 'Pitcher'),
        (2, 'Catcher'),
        (3, 'First baseman'),
        (4, 'Second baseman'),
        (5, 'Third baseman'),
        (6, 'Shortstop'),
        (7, 'Left fielder'),
        (8, 'Center fielder'),
        (9, 'Right fielder'),
        (10, 'Designated hitter'),
    )

    lineup = models.ForeignKey(Lineup)
    player = models.ForeignKey(Player)
    batting_position = models.IntegerField()
    defensive_position = models.IntegerField(choices=POSITIONS)

    class Meta:
        verbose_name_plural = 'lineup entries'
        ordering = ['batting_position']


class OffensiveStats(models.Model):
    participating_team = models.OneToOneField(ParticipatingTeam)
    at_bats = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    home_runs = models.IntegerField()
    rbis = models.IntegerField()
    sac_hits = models.IntegerField()
    sac_flies = models.IntegerField()
    hbps = models.IntegerField()
    walks = models.IntegerField()
    ibbs = models.IntegerField()
    strikeouts = models.IntegerField()
    stolen_bases = models.IntegerField()
    caught_stealing = models.IntegerField()
    gidps = models.IntegerField()
    reached_on_interference = models.IntegerField()

    class Meta:
        verbose_name_plural = 'offensive stats'


class DefensiveStats(models.Model):
    participating_team = models.OneToOneField(ParticipatingTeam)
    putouts = models.IntegerField()
    assists = models.IntegerField()
    passed_balls = models.IntegerField()
    double_plays = models.IntegerField()
    triple_plays = models.IntegerField()

    class Meta:
        verbose_name_plural = 'defensive stats'


class PitchingStats(models.Model):
    participating_team = models.OneToOneField(ParticipatingTeam)
    pitchers = models.IntegerField()
    earned_runs = models.IntegerField()
    team_earned_runs = models.IntegerField()
    wild_pitches = models.IntegerField()
    balks = models.IntegerField()

    class Meta:
        verbose_name_plural = 'pitching stats'