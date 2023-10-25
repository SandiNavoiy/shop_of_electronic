from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.pagination import ProductPaginator
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания продукта"""

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductListAPIView(generics.ListAPIView):
    """Контроллер для списка продукта"""

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProductPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра данных продукта"""

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления данных продукта"""

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления данных продукта"""

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
