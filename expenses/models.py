from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 1. Define the new Category model
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True) # e.g., '🍔', '🚌'
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

# 2. Update Expense model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Changed from CharField to ForeignKey
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    # Added timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.amount}"