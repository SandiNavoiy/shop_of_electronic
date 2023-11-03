from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from retail_network.models import Retail_network
from retail_network.pagination import Retail_networkPaginator
from retail_network.serializers import Retail_networkSerializer


class Retail_networkCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания звена сети продаж"""

    serializer_class = Retail_networkSerializer
    # permission_classes = [IsAuthenticated]


class Retail_networkListAPIView(generics.ListAPIView):
    """Контроллер для списка звеньев сети продаж"""

    serializer_class = Retail_networkSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = Retail_networkPaginator
    queryset = Retail_network.objects.all()


class Retail_networkRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра звена сети продаж"""

    serializer_class = Retail_networkSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Retail_network.objects.all()


class Retail_networkUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления данных звена сети продаж"""

    serializer_class = Retail_networkSerializer
    # permission_classes = [IsAdminUser]
    queryset = Retail_network.objects.all()


class Retail_networkDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления данных звена сети продаж"""

    serializer_class = Retail_networkSerializer
    # permission_classes = [IsAdminUser]
    queryset = Retail_network.objects.all()
