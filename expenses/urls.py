from django.urls import path
from . import views

urlpatterns = [
    # Home Dashboard
    path('', views.home, name='home'),
    
    # Authentication
    path('signup/', views.signup, name='signup'),
    
    # 🌟 THE MISSING LINKS PUT BACK 🌟
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
]