from django.db.models import Sum
from rest_framework import serializers

from expenses.models import Expense, Category


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'category',
            'title',
            'description',
            'price')


class ExpenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'category',
            'title',
            'description',
            'price',
            'account',
            'date_created')

        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    category_expenses = ExpenseSerializer(many=True)
    total = serializers.SerializerMethodField('get_total_expenses')


    def get_total_expenses(self, obj):
        return obj.category_expenses.aggregate(Sum('price'))

    class Meta:
        model = Category
        fields = ('id', 'title','total' , 'category_expenses')
