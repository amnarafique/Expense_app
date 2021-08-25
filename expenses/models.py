from django.db import models

from users.models import Account


class Category(models.Model):
    title = models.CharField(max_length=225)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT,
                                 related_name='category_expenses', default=1)

    account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                related_name='user_expense')

    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title