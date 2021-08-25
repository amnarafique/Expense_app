from django.shortcuts import render
from rest_framework import generics

from users.serializers import AccountRegistrationSerializer


class AccountRegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer
