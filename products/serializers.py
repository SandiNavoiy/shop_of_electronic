from rest_framework import serializers

from factory.models import Factory
from factory.serializers import FactorySerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Factory.objects.all())

    class Meta:
        model = Product
        fields = "__all__"  # Поля для отображения
