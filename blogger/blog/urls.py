from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<str:slug>/', views.PostView.as_view(), name='post'),
    path('create/', views.CreatePostView.as_view(), name='create'),
]
