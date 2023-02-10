from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm
from .models import User
from blog.models import Post


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        return context


class LoginUserView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm


class LogoutUserView(LogoutView):
    pass
