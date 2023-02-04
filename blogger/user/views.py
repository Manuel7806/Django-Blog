from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import RegisterForm
from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'


class IndexView(TemplateView):
    template_name = 'home.html'
