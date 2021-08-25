from django.urls import path

from users.views import AccountRegisterAPIView

urlpatterns = [
    path('register/', AccountRegisterAPIView.as_view(), name='register')
]