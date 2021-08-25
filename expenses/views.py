
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expense, Category
from expenses.serializers import ExpenseSerializer
from users.models import Account


@csrf_exempt
@api_view(['POST'])
def expense_create_view(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        user = request.user
        account = Account.objects.filter(user=user).first()
        category = Category.objects.filter(id=category_id).first()
        expense = Expense.objects.create(
            category=category,
            title=title,
            description=description,
            price=price,
            account=account
        )

    return HttpResponse(expense, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def expenses_list_api_view(request):
    user = request.user
    account = Account.objects.filter(user=user).first()
    account_expenses = Expense.objects.filter(account=account)

    serializer = ExpenseSerializer(account_expenses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def expense_retrieve_api_view(request, pk):
    expense = Expense.objects.filter(id=pk).first()
    serializer = ExpenseSerializer(expense)
    return Response(data=serializer.data, status=status.HTTP_200_OK)