from django.shortcuts import render
from rest_framework import generics

from users.serializers import AccountRegistrationSerializer


class AccountRegisterAPIView(generics.CreateAPIView):

    """
    This endpoint registers users based on fields
    """


    serializer_class = AccountRegistrationSerializer
