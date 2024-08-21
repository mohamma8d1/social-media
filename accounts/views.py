from django.contrib.auth import get_user_model

from rest_framework import generics

from .serializers import RegisterSerializer

user = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = RegisterSerializer

