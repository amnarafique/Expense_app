from django.contrib.auth.models import User
from users.models import Account


class TopUpService:

    @classmethod
    def top_up(cls, user: User, balance: float) -> None:
        account = Account.objects.filter(user=user).first()
        account.balance += float(balance)
        account.save()
