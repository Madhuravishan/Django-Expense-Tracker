from django.contrib import admin
from django.urls import path, include
from expenses import views

urlpatterns = [
    # The Admin Panel
    path('admin/', admin.site.urls), 
    
    # Your built-in Login/Logout paths 
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 🌟 THIS IS THE NEW LINE FOR SIGNUP 🌟
    path('signup/', views.signup, name='signup'),
    
    # Your Home Dashboard
    path('', views.home, name='home'), 
]