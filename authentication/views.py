from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class MeAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
