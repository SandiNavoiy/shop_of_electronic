from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from employee.apps import EmployeeConfig
from employee.views import (
    EmployeeCreateAPIView,
    EmployeeListAPIView,
    EmployeeRetrieveAPIView,
    EmployeeUpdateAPIView,
    EmployeeDestroyAPIView,
)

app_name = EmployeeConfig.name

# Урлы для приложения пользователя с токенами
urlpatterns = [
    path("create/", EmployeeCreateAPIView.as_view(), name="employee_create"),
    path("list/", EmployeeListAPIView.as_view(), name="employee_list"),
    path(
        "deteil/<int:pk>/",
        EmployeeRetrieveAPIView.as_view(),
        name="employee_deteil",
    ),
    path(
        "update/<int:pk>/",
        EmployeeUpdateAPIView.as_view(),
        name="employee_update",
    ),
    path(
        "delete/<int:pk>/",
        EmployeeDestroyAPIView.as_view(),
        name="employee_delete",
    ),
    # Работа с токенами
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
