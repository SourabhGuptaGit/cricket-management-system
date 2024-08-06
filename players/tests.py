from django.test import TestCase
from teams.models import Team
from .models import Player

class PlayerModelTest(TestCase):
    def setUp(self):
        team = Team.objects.create(name='Team A', logo_uri='http://example.com/logo_a.png', club_state='State A')
        Player.objects.create(first_name='John', last_name='Doe', image_uri='http://example.com/john_doe.png', jersey_number=10, country='Country A', team=team)

    def test_player_creation(self):
        player = Player.objects.get(first_name='John')
        self.assertEqual(player.first_name, 'John')
        self.assertEqual(player.last_name, 'Doe')
        self.assertEqual(player.image_uri, 'http://example.com/john_doe.png')
        self.assertEqual(player.jersey_number, 10)
        self.assertEqual(player.country, 'Country A')
