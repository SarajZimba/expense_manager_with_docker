from django.urls import path 
from .views import ExpenseFormView, ExpenseList, ExpenseUpdateView
urlpatterns = [
    path('expense-create/', ExpenseFormView.as_view(), name="expense-create"),
    path('', ExpenseList.as_view(), name="expense-list"),
 path('expenses/<int:pk>/update/', ExpenseUpdateView.as_view(), name='update_expense'),
]