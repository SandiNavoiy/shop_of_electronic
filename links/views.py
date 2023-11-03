from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from links.models import Link
from links.serializers import LinkSerializer


class LinkCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания координат продавца"""

    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра данных продавца"""

    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]
    queryset = Link.objects.all()


class LinkUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления данных продавца"""

    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]
    queryset = Link.objects.all()


class LinkDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления данных продавца"""

    serializer_class = LinkSerializer
    permission_classes = [IsAdminUser]
    queryset = Link.objects.all()
