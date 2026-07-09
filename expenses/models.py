from django.db import models
from django.contrib.auth.models import User  
from django.utils import timezone

class Expense(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.amount}"
    
    def __clstr__(self):
        return self.title