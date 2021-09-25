from rest_framework import serializers
from .model import League


# Serializers define the API representation.
class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = "__all__"
