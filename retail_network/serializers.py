from rest_framework import serializers

from retail_network.models import Retail_network


class Retail_networkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""

    class Meta:
        model = Retail_network
        fields = "__all__"  # Поля для отображе
