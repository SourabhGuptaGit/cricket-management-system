from django.core.management.base import BaseCommand
from teams.models import Team
from matches.models import Match
import random

class Command(BaseCommand):
    help = 'Generate random fixtures for matches'

    def handle(self, *args, **kwargs):
        teams = list(Team.objects.all())
        random.shuffle(teams)
        
        for i in range(0, len(teams), 2):
            if i+1 < len(teams):
                match = Match.objects.create(team_1=teams[i], team_2=teams[i+1])
                self.stdout.write(f'Match created: {teams[i].name} vs {teams[i+1].name}')
