from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]