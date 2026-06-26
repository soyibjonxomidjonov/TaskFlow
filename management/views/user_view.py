from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model

from management.serializers import UserSerializerConfig

# from management.filters import UserFilter
from rest_framework import viewsets
from django_filters import rest_framework as django_filters
# from django_filters import rest_framework as django_filters
# from rest_framework import filters

User = get_user_model()

class CustomPagination(PageNumberPagination):
    page_size = 5


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializerConfig

    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['phone_number', 'email', 'first_name']

    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser()]  # ← faqat admin user yarata oladi
        return [IsAuthenticated()]
