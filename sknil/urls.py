from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from apps.core.views import frontpage, signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('', frontpage, name='frontpage'),
]
