from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication
from rest_framework import exceptions
from employee.models import Employee
from employee.serializers import EmployeeSerializer


# Create your views here.
class EmployeeCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""

    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True
        user.save()


class EmployeeListAPIView(generics.ListAPIView):
    """Контроллер для списка пользователей"""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра пользователя"""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления пользователя"""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class EmployeeDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления пользователя"""

    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]


class IsActiveUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user = request.user
        if user and user.is_active:
            return (user, None)
        raise exceptions.AuthenticationFailed("Пользователь не активен")
