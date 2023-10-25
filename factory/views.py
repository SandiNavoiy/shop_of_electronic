
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from factory.pagination import FactoryPaginator
from factory.serializers import FactorySerializer


class FactoryCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания производителя"""

    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]

class FactoryListAPIView(generics.ListAPIView):
    """Контроллер для списка производителей"""

    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FactoryPaginator

class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра данных производителя"""

    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated]

class FactoryUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления данных производителя"""

    serializer_class = FactorySerializer
    permission_classes = [IsAdminUser]

class FactoryDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления данных производителя"""

    serializer_class = FactorySerializer
    permission_classes = [IsAdminUser]