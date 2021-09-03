from celery import shared_task
from django.db.models import F

from users.models import Account


@shared_task
def pay_salary():
    Account.objects.all().update(balance=F('salary') + F('balance'))
