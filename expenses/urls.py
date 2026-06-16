from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The Admin Panel
    path('admin/', admin.site.urls), 
    
    # Built-in Django login/logout paths
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 🌟 THIS KNOTS EVERYTHING TOGETHER 🌟
    # This tells Django to look inside expenses/urls.py for home, signup, edit, and delete!
    path('', include('expenses.urls')), 
]