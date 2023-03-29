from django.db import models


class Hero(models.Model):
    name = models.CharField(verbose_name='hero name', max_length=50, null=False, blank=False, unique=True)
    alias = models.CharField(verbose_name='hero`s real name', max_length=50, null=False, blank=False, unique=True)
    team = models.ForeignKey(verbose_name='hero`s team', to='Team', on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name='hero`s activity', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Team(models.Model):

    class TeamName(models.TextChoices):
        JUSTICE_LEAGUE = 'justice_league', 'Justice League'
        THE_SEVEN = 'the_seven', 'The Seven'
        DOOM_PATROL = 'doom_patrol', 'Doom Patrol'
        NO_TEAM = 'no_team', 'No team provided'
        
        __empty__ = 'Unknown'


    team_name = models.CharField(verbose_name='hero`s team name', max_length=20, choices=TeamName.choices, default=TeamName.NO_TEAM)

    def __str__(self):
        return self.team_name
