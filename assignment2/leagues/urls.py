from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

from assignment2.teams.serializer import TeamSerializer
from assignment2.teams.model import Team
from .model import League
from .serializer import LeagueSerializer

class LeagueViewSet(viewsets.ViewSet):
    queryset = League.objects.all()

    # GET all Leagues
    def list(self, request):
        queryset = League.objects.all()
        serializer = LeagueSerializer(queryset, many=True)
        return Response(serializer.data)

    # GET one League
    def retrieve(self, request, pk=None):
        queryset = League.objects.all()
        league = get_object_or_404(queryset, pk=pk)
        serializer = LeagueSerializer(league)
        return Response(serializer.data)

    # POST one League
    def create(self, request):
        serializer = LeagueSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                existing_league = League.objects.filter(
                    name=serializer.validated_data["name"],
                    sport=serializer.validated_data["sport"]
                )
                if len(existing_league) > 0:
                    return Response(
                        LeagueSerializer(existing_league[0]).data,
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
    
    # GET Teams for a League
    @action(detail=True, url_path="teams")
    def teams(self, request, pk=None):
        queryset = League.objects.all()
        league = get_object_or_404(queryset, pk=pk)
        teams_queryset = Team.objects.filter(
            league_id__in=[league]
        )
        serializer = TeamSerializer(teams_queryset, many=True)
        return Response(serializer.data)

    # POST one Team for a League
    @teams.mapping.post
    def create_team(self, request, pk=None):
        existing_league = League.objects.filter(pk=pk)
        if len(existing_league) == 0:
            return Response({
                    "status": "Unprocessable Entity",
                    "errors": {
                        "league_id": ["League does not exist"]
                    }
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        league = existing_league[0]
        request.data["league_id"] = league.id
        serializer = TeamSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                existing_team = Team.objects.filter(
                    name=serializer.validated_data["name"],
                    city=serializer.validated_data["city"]
                )
                if len(existing_team) > 0:
                    return Response(
                        TeamSerializer(existing_team[0]).data,
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
