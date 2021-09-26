from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

from assignment2.players.model import Player
from assignment2.players.serializer import PlayerSerializer

from .model import Team
from .serializer import TeamSerializer

class TeamViewSet(viewsets.ViewSet):
    queryset = Team.objects.all()

    # GET all Teams
    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    # GET one Team
    def retrieve(self, request, pk=None):
            queryset = Team.objects.all()
            team = get_object_or_404(queryset, pk=pk)
            serializer = TeamSerializer(team)
            return Response(serializer.data)

    # GET Players for a Team
    @action(detail=True, url_path="players")
    def players(self, request, pk=None):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        players_queryset = Player.objects.filter(
            team_id__in=[team]
        )
        serializer = PlayerSerializer(players_queryset, many=True)
        return Response(serializer.data)
