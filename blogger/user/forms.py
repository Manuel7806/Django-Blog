from django import forms
from django.contrib.auth.hashers import make_password
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
