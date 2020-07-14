from django.urls import path

from .views import dashboard
from apps.bookmark.views import categories

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('categories/', categories, name='categories'),
]