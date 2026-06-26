from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets


from management.models import Task, Employee
from management.serializers import TaskSerializerConfig, EmployeeSerializerConfig
from management.permissions import IsStaffOrReadOnly

from .user_view import CustomPagination

# from django_filters import rest_framework as django_filters
# from rest_framework import filters
# from products.filters.misc_filter import CommentsFilter, OrderFilter, OrderItemsFilter



class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # search_fields = []
    pagination_class = CustomPagination



class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # search_fields = []
    pagination_class = CustomPagination