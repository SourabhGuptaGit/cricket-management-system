from django.db import models

class Team(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo_uri = models.URLField(max_length=200)
    club_state = models.CharField(max_length=100)

    def __str__(self):
        return self.name
