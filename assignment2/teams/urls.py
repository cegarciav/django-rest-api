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

    # DELETE one Team and its Players
    def destroy(self, request, pk=None):
            queryset = Team.objects.all()
            team = get_object_or_404(queryset, pk=pk)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

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

    # POST one Player for a Team
    @players.mapping.post
    def create_player(self, request, pk=None):
        existing_team = Team.objects.filter(pk=pk)
        if len(existing_team) == 0:
            return Response({
                    "status": "Unprocessable Entity",
                    "errors": {
                        "team_id": ["Team does not exist"]
                    }
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        team = existing_team[0]
        request.data["team_id"] = team.id
        request.data["times_trained"] = 0
        serializer = PlayerSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                existing_player = Player.objects.filter(
                    name=serializer.validated_data["name"],
                    position=serializer.validated_data["position"]
                )
                if len(existing_player) > 0:
                    return Response(
                        PlayerSerializer(existing_player[0]).data,
                        status=status.HTTP_409_CONFLICT
                    )
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({
                    "status": "Bad Request",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
