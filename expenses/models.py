from django.db import models
from django.contrib.auth.models import User  # <-- 1. Add this import at the top

class Expense(models.Model):
    # <-- 2. ADD THIS NEW LINE -->
    # (default=1 means all your old expenses will be assigned to your admin account)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.amount}"