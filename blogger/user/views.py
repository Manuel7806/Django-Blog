from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm, LoginForm
from .models import User, UserInfo


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        form = self.form_class(request.POST)
        user = authenticate(username=username, password=password)

        if user is not None:
            u = User.objects.get(username=username)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile', kwargs={'pk': u.pk}))
            else:
                HttpResponse('Inactive User')
        else:
            return HttpResponseRedirect(reverse('login'))

        return render(request, 'login.html', context={'form': form})

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, context={'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = UserInfo.objects.get(user=self.object)
        return context
