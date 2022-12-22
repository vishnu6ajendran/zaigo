

from django.urls import path
from users.views import list_user,fetch_user

urlpatterns = [
    path('list',list_user, name="list"),
    path('fetch',fetch_user, name="fetch"),
    path('update',fetch_user, name="fetch"),
]