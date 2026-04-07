from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')), # Your app URLs
    
    # --- ADD THIS NEW LINE ---
    path('accounts/', include('django.contrib.auth.urls')), 
]