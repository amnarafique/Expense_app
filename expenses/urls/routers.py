
from expenses.views import ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ExpenseViewSet, basename='user')
urlpatterns = router.urls

