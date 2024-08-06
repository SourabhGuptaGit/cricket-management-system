from django.shortcuts import render
from .models import PointsTable

def points_table(request):
    points = PointsTable.objects.all().order_by('-points')
    return render(request, 'points/points_table.html', {'points': points})
