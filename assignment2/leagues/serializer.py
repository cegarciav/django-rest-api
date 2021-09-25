from rest_framework import serializers
from .model import League


# Serializers define the API representation.
class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = "__all__"
        read_only_fields = (
            "id",
            "teams",
            "players",
            "self",
        )
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "sport": {"required": True, "allow_blank": False}
        }
