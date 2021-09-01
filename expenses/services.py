from django.contrib.auth.models import User
from users.models import Account


class TopUpService:

    @classmethod
    def make_balance_float(cls, balance):
        try:
            amount = float(balance)
        except ValueError:
            return 0
        return amount

    @classmethod
    def top_up(cls, user: User, balance: float) -> None:
        amount = cls.make_balance_float(balance)
        account = Account.objects.filter(user=user)
        account.balance += amount
        account.save()