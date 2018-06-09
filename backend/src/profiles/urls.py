from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.current_user),
    path('users/', views.UserList.as_view()),
]