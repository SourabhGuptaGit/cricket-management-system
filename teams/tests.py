from django.test import TestCase
from .models import Team

class TeamModelTest(TestCase):
    def setUp(self):
        Team.objects.create(name='Team A', logo_uri='http://example.com/logo_a.png', club_state='State A')

    def test_team_creation(self):
        team = Team.objects.get(name='Team A')
        self.assertEqual(team.name, 'Team A')
        self.assertEqual(team.logo_uri, 'http://example.com/logo_a.png')
        self.assertEqual(team.club_state, 'State A')
