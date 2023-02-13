from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm, UserSettingsForm
from .models import User
from blog.models import Post


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        return context


class SettingsView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'settings.html'
    form_class = UserSettingsForm
    success_url = '/profile/{slug}/'


class LoginUserView(LoginView):
    template_name = 'login.html'
    success_url = '/profile/{slug}/'
    authentication_form = LoginForm


class LogoutUserView(LogoutView):
    pass
