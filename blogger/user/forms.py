from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegisterForm(forms.ModelForm):
    def clean_password(self):
        password = self.cleaned_data['password']
        password = make_password(password)

        return password

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email=email)

        if user:
            raise forms.ValidationError(
                'That email is in use by another member already, if you have an account you can login')

        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username)

        if not user:
            raise forms.ValidationError('Incorrect username')

        return username

    # def clean_password(self):
    #     # This is the part I need help with

    #     # NOTE This code does nothing, just used to
    #     # display the functionality I want to implement

    #     password = self.cleaned_data['password']

    #     if not check_password(password):
    #         raise forms.ValidationError('Incorrect password')

    #     return password
