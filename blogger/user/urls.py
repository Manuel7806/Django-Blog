from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/<str:slug>/', views.ProfileView.as_view(), name='profile'),
    # path('profile/<str:slug>/', views.Profile.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
