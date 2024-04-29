from django.db import models
from root.utils import BaseModel
from user.models import Customer

class ExpenseCategory(BaseModel):
    title = models.CharField(max_length= 255, null=True, blank=True)
    def __str__(self):
        return self.title

class Expense(BaseModel):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50)
    expense_category = models.ForeignKey(ExpenseCategory, models.CASCADE, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
