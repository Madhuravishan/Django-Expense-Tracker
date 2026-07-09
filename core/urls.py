from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The Admin Panel
    path('admin/', admin.site.urls), 
    
    # Built-in Django login/logout paths
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Send all other traffic to the expenses app
    path('', include('expenses.urls')), 
]