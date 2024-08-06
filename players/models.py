from django.db import models
from teams.models import Team

class Player(models.Model):
    identifier = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image_uri = models.URLField(max_length=200)
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    # Player history
    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
