from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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

    # POST one Team
    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                existing_team = Team.objects.filter(
                    name=serializer.validated_data["name"],
                    sport=serializer.validated_data["sport"]
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
