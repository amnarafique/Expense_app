from django.urls import path

from users.views import AccountRegisterAPIView, AccountDetailAPIView

urlpatterns = [
    path('register/', AccountRegisterAPIView.as_view(), name='register'),
    path('<int:pk>/', AccountDetailAPIView.as_view(), name='detail')
]