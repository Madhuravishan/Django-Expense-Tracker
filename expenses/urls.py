from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    
    # NEW LINE:
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
]