from django.contrib import admin
from .models import PointsTable

@admin.register(PointsTable)
class PointsTableAdmin(admin.ModelAdmin):
    list_display = ('team', 'points', 'matches_played', 'matches_won', 'matches_lost')
