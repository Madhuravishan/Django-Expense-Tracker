from django import forms
from .models import Expense, Category # Make sure to import Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            # We change this so it shows a dropdown of Categories
            'category': forms.Select(attrs={'class': 'form-control'}),
        }