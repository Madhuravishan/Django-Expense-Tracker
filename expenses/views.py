from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm  # <-- NEW IMPORT
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

# --- NEW SIGNUP VIEW ---
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- EXISTING VIEWS ---
@login_required
def home(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Pause the save, attach the user, then save
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    # FILTER THE DATABASE: Only get the current user's expenses
    expenses = Expense.objects.filter(user=request.user)
    
    # Calculate the total of all expenses for this user
    total_expenses = expenses.aggregate(Sum('amount'))
    sum_amount = total_expenses['amount__sum']
    
    # Fallback if there are no expenses yet
    if sum_amount is None:
        sum_amount = 0

    # Calculate totals per category for the charts
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
    # Security check: Only delete if the logged-in user owns it
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('home')

@login_required
def update_expense(request, expense_id):
    # Security check: Only update if the logged-in user owns it
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
            
    return render(request, 'expenses/edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})