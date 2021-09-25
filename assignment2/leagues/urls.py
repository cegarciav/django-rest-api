from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .model import League
from .serializer import LeagueSerializer

class LeagueViewSet(viewsets.ViewSet):
    queryset = League.objects.all()

    def list(self, request):
        queryset = League.objects.all()
        serializer = LeagueSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
            queryset = League.objects.all()
            league = get_object_or_404(queryset, pk=pk)
            serializer = LeagueSerializer(league)
            return Response(serializer.data)
