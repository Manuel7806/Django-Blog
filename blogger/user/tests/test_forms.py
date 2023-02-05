from django.test import TestCase
from user.forms import RegisterForm


class TestRegisterForm(TestCase):
    def test_form_valid(self):
        form = RegisterForm(data={'first_name': 'John', 'last_name': 'Doe',
                            'username': 'johndoe', 'email': 'johndoe@site.com', 'password': 'password'})
        self.assertTrue(form.is_valid())
