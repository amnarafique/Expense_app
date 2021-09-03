from django.core.management import BaseCommand
from django.db.models import F

from users.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        Account.objects.all().update(balance=F('salary') + F('balance'))

