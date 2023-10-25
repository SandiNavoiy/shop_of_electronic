from rest_framework import serializers

from factory.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""

    class Meta:
        model = Factory
        fields = "__all__"  # Поля для отображения
