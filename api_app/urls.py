
from django.urls import path
from .views import CustomUserListView

urlpatterns = [
    path('users/', CustomUserListView.as_view(), name='api-user-list'),
]