from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from .model import Player
from .serializer import PlayerSerializer

class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()

    # GET all Players
    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

    # GET one Player
    def retrieve(self, request, pk=None):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    # DELETE one Player
    def destroy(self, request, pk=None):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # PUT Train one Player
    @action(detail=True, methods=["put"], url_path="train")
    def train_player(self, request, pk=None):
        queryset = Player.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        player.times_trained += 1
        player.save()
        return Response(status=status.HTTP_200_OK)
