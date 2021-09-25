from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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
