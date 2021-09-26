from rest_framework import serializers
from .model import Player


# Serializers define the API representation.
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
        read_only_fields = (
            "id",
            "league",
            "team",
            "self",
        )
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False},
            "age": {"allow_null": False},
            "position": {"required": True, "allow_blank": False}
        }
