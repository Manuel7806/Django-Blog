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


# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('home')

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)

    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)

    #     if form.is_valid():
    #         first_name = form.cleaned_data.get('first_name')
    #         last_name = form.cleaned_data.get('last_name')
    #         username = form.cleaned_data.get('username')
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')

    #         form.save()
    #         return HttpResponseRedirect(reverse_lazy('home'))

    #     return render(request, self.template_name, {'form': form})


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'


class IndexView(TemplateView):
    template_name = 'home.html'
