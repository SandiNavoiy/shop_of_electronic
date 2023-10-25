from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""

    class Meta:
        model = Product
        fields = "__all__"  # Поля для отображе
