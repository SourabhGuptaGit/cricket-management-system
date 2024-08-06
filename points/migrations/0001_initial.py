# Generated by Django 5.0.7 on 2024-08-05 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('matches_played', models.IntegerField(default=0)),
                ('matches_won', models.IntegerField(default=0)),
                ('matches_lost', models.IntegerField(default=0)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]