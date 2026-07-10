from django.urls import path
from . import views

urlpatterns = [
    # Home Dashboard
    path('', views.home, name='home'),
    
    # 🌟 NEW: The Signup Page 🌟
    path('signup/', views.signup, name='signup'),
    
    # Edit and Delete paths
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]