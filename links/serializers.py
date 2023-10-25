from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""

    class Meta:
        model = Link
        fields = "__all__"  # Поля для отображе
