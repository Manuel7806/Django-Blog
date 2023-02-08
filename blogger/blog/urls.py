from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<str:username>/<str:slug>/',
         views.PostView.as_view(), name='post'),
    path('create/', views.CreatePostView.as_view(), name='create'),
]
