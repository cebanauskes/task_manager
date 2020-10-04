from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = UserSerializer
