from django.urls import path
from .views import CreateUser, ListUsers

urlpatterns = [
    path('createUser/', CreateUser.as_view(), name='create_user'),
    path('listUsers/', ListUsers.as_view(), name='list_users'),
]
