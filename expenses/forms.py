from django import forms
from .models import Expense
class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['title','amount','date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.TextInput(attrs={'list': 'category-list', 'placeholder': 'Select or type new...'})
            }
        