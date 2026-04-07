from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.db.models import Sum
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required 

@login_required
def home(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # 1. Pause the save, attach the user, then save!
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    # 2. FILTER THE DATABASE: Only get the current user's expenses
    expenses = Expense.objects.filter(user=request.user)
    
    total_expenses = expenses.aggregate(Sum('amount'))

    sum_amount = total_expenses['amount__sum']
    if sum_amount is None:
        sum_amount = 0

    category_sums = expenses.values('category').annotate(category_total=Sum('amount'))
    
    chart_labels = []
    chart_data = []
    
    for item in category_sums:
        chart_labels.append(item['category'])
        chart_data.append(float(item['category_total']))

    return render(request, 'expenses/home.html', {
        'expenses': expenses,
        'total': sum_amount,
        'form': form,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    })

@login_required
def delete_expense(request, expense_id):
    # 3. Security check: Only delete if the logged-in user owns it
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('home')

@login_required
def update_expense(request, expense_id):
    # 4. Security check: Only update if the logged-in user owns it
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
        
    return render(request, 'expenses/edit.html', {'form': form})