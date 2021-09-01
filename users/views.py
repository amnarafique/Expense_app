from django.shortcuts import render
from rest_framework import generics

from rest_framework import permissions
from users.models import Account
from users.permissions import IsOwner
from users.serializers import AccountRegistrationSerializer, AccountDetailSerializer


class AccountRegisterAPIView(generics.CreateAPIView):

    """
    This endpoint registers users based on fields
    """

    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)


class AccountDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountDetailSerializer
    queryset = Account.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)


