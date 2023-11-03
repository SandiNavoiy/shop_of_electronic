from rest_framework import serializers

from links.models import Link
from products.models import Product
from retail_network.models import Retail_network


class Retail_networkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукты"""

    contacts = serializers.PrimaryKeyRelatedField(queryset=Link.objects.all())  # Для поля contacts
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())  # Для поля products
    supplier = serializers.PrimaryKeyRelatedField(queryset=Retail_network.objects.all(), required=False,
                                                  allow_null=True)
    class Meta:
        model = Retail_network
        fields = "__all__"  # Поля для отображе
