from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from .models import User
from blog.models import Post


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        return context
