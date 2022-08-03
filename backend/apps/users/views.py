import re
from typing import Generic
from .mixins import CustomLoginRequiredMixin
from .serializers import UserSignUpSerializer
from .models import User
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer


class UserCheckLogIn(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSignInSerializer([request.login_user], many=True)
        return response(serializer.data[0])


class UserList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = User.objects.all()[:20]
    serializer_class = UserSerializer
