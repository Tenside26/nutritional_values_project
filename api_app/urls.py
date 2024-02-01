
from django.urls import path
from .views import CustomUserListView

urlpatterns = [
    path('users-list/', CustomUserListView.as_view(), name='api-users-list'),
]