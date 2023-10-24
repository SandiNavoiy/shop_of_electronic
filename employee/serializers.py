from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # Сериализатор для пользователя
    class Meta:
        model = Employee
        fields = "__all__"