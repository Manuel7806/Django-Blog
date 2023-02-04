from django.test import TestCase
from .models import User, UserInfo


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        username='johndoe656', email='johndoe@site.com', password='johnpassworddoe')

    def test_get_user(self):
        self.assertEqual(str(self.user), 'johndoe656')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'John Doe')

    def test_first_name(self):
        self.assertEqual(self.user.first_name, 'John')

    def test_last_name(self):
        self.assertEqual(self.user.last_name, 'Doe')

    def test_email(self):
        self.assertEqual(self.user.email, 'johndoe@site.com')


class TestUserInfo(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        username='johndoe656', email='johndoe@site.com', password='johnpassworddoe')
        self.info = UserInfo.objects.create(
            dob='1990-10-5', sex='Male', user=self.user)

    # Pass Test

    def test_get_user_info(self):
        self.assertEqual(str(self.info), 'johndoe656')

    def test_get_dob(self):
        self.assertEqual(self.info.dob, '1990-10-5')

    def test_get_sex(self):
        self.assertEqual(self.info.sex, 'Male')

    # Fail Test

    def test_get_user_info_fail(self):
        self.assertEqual(str(self.info), 'johndoe')
