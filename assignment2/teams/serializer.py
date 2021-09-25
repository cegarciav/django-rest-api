from rest_framework import serializers
from .model import Team


# Serializers define the API representation.
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = (
            "id",
            "league",
            "players",
            "self",
        )
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "city": {"required": True, "allow_blank": False}
        }
