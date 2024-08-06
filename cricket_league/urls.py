from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teams.urls')),
    # path('teams/', include('teams.urls')),
    path('matches/', include('matches.urls')),
    path('points/', include('points.urls')),
]
