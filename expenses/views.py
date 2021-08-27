
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expense, Category
from expenses.permissions import IsOwner
from expenses.serializers import ExpenseSerializer, ExpenseDetailSerializer
from users.models import Account
from rest_framework import generics
from rest_framework import permissions


class ExpenseListCreateAPIVIew(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(account=self.request.user.account)

    def get_queryset(self):
        return Expense.objects.filter(account=self.request.user.account)


class ExpenseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)



# class ExpenseCreateAPIView(generics.CreateAPIView):
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         serializer.save(account=self.request.user.account)
#
#
# class ExpenseListAPIView(generics.ListAPIView):
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return Expense.objects.filter(account=self.request.user.account)
#
#
# class ExpenseRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseDetailSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
#
# class ExpenseUpdateAPIView(generics.UpdateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#
#
# class ExpenseDeleteAPIView(generics.DeleteAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwner)















# @csrf_exempt
# @api_view(['POST'])
# def expense_create_view(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('category')
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         user = request.user
#         account = Account.objects.filter(user=user).first()
#         category = Category.objects.filter(id=category_id).first()
#         expense = Expense.objects.create(
#             category=category,
#             title=title,
#             description=description,
#             price=price,
#             account=account
#         )
#
#     return HttpResponse(expense, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def expenses_list_api_view(request):
#     user = request.user
#     account = Account.objects.filter(user=user).first()
#     account_expenses = Expense.objects.filter(account=account)
#
#     serializer = ExpenseSerializer(account_expenses, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def expense_retrieve_api_view(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#     if expense.account.user != request.user:
#         return Response({"success": False,
#                          "message": "you don't have permissions"},
#                         status=status.HTTP_403_FORBIDDEN)
#
#     serializer = ExpenseSerializer(expense)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def expense_put_update_api_view(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#     if expense.account.user != request.user:
#         return Response({"success": False,
#                          "message": "you don't have permissions"},
#                         status=status.HTTP_403_FORBIDDEN)
#
#     category = Category.objects.filter(id=request.data.get('category')).first()
#
#     expense.category = category
#     expense.title = request.data.get('title')
#     expense.price = request.data.get('price')
#     expense.description = request.data.get('description')
#     expense.save()
#
#     return Response(data='OK', status=status.HTTP_200_OK)
#
#
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def expense_delete_api_view(request, pk):
#     expense = Expense.objects.filter(id=pk).first()
#     if expense.account.user != request.user:
#         return Response({"success": False,
#                          "message": "you don't have permissions"},
#                         status=status.HTTP_403_FORBIDDEN)
#
#     expense.delete()
#     return Response('Deleted', status=status.HTTP_200_OK)
#
#
