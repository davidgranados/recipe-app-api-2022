"""
Serializers fro recipe APIs
"""
from rest_framework import serializers

from core.models import Recipe


class ReciperSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ("id", "title", "time_minutes", "price", "description", "link")
        read_only_fields = ("id",)
