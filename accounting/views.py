from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import View, UpdateView, DeleteView
from .models import Expense, ExpenseCategory
from django.db.models import Sum
from .forms import ExpenseForm


class ExpenseFormView(View):
    template_name = 'expense/expense_form.html'

    def get(self, request, *args, **kwargs):
        categories = ExpenseCategory.objects.filter(is_deleted=False)
        context = {"categories": categories}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        titles = request.POST.getlist('title[]')
        amounts = request.POST.getlist('amount[]')
        dates = request.POST.getlist('date[]')
        notes = request.POST.getlist('note[]')
        categories = request.POST.getlist('category[]')

        # Iterate through the submitted data to create Expense instances
        for title, amount, date, note, category_id in zip(titles, amounts, dates,notes, categories):
            category = ExpenseCategory.objects.get(pk=category_id)
            Expense.objects.create(title=title, amount=amount, date=date, notes=note, expense_category=category)

        # Redirect to a success page or render a success message
        return HttpResponseRedirect(reverse('expense-list'))  # Replace 'success_page' with your actual URL name
    
class ExpenseList(View):
    template_name = 'expense/expense_list.html'

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.filter(is_deleted=False)

        category_totals = Expense.objects.values('expense_category__title').annotate(total_amount=Sum('amount'))
        total_expense_amount = expenses.aggregate(total_amount=Sum('amount'))['total_amount']

        context = {'expenses': expenses, 'total_expense': total_expense_amount, 'category_totals':category_totals}
        return render(request, self.template_name, context)

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    # fields = ['title', 'amount', 'date', 'notes']
    template_name = 'expense/expense_update.html'  # Template for updating expense
    success_url = reverse_lazy('expense-list')

# 

    


