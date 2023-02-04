from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.IndexView.as_view(), name='home'),
]
