from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import RegisterForm
from .models import User, UserInfo


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = UserInfo.objects.get(user=self.object)
        context['display_options'] = ['email', 'dob', 'sex', 'active']
        return context


class IndexView(TemplateView):
    template_name = 'home.html'
