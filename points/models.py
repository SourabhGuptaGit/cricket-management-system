from django.db import models
from teams.models import Team

class PointsTable(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team.name} - {self.points} Points'
