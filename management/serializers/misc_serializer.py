from rest_framework import serializers
from management.models import Employee, Task


class EmployeeSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ['id', 'created_at']



class TaskSerializerConfig(serializers.ModelSerializer):
    employee_name = serializers.CharField(
        source='employee.full_name',
        read_only=True
    )
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']
