from django.urls import path
from api.views.accounting import ExpenseList, ExpenseDetail

urlpatterns = [
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
]
