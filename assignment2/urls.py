from django.urls import path, include
from rest_framework import routers

from assignment2.leagues.urls import LeagueViewSet
from assignment2.teams.urls import TeamViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'leagues', LeagueViewSet, basename="League")
router.register(r'teams', TeamViewSet, basename="Team")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
