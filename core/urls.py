from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Make sure this is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')), # Your app URLs
    
    # --- ADD THIS LINE FIRST to force the custom template ---
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Keep this line below it for logouts, password resets, etc.
    path('accounts/', include('django.contrib.auth.urls')), 
]