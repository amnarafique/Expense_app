from django.contrib import admin

from expenses.models import Category, Expense

admin.site.register(Category)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'account',
        'price',
        'date_created',)

    search_fields = (
        'title',
        'account'

    )

    list_filter = (
        'category',
        'price'
    )
