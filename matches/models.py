from django.db import models
from teams.models import Team

class Match(models.Model):
    team_1 = models.ForeignKey(Team, related_name='team_1', on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name='team_2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.team_1.name} vs {self.team_2.name}'
