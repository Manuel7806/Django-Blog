from django.test import TestCase
from user.models import User
from secrets import token_urlsafe

dob = '1991-04-23'
token = token_urlsafe()


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        username='johndoe656', email='johndoe@site.com', password='johnpassworddoe', dob=dob)

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

    def test_get_dob(self):
        self.assertEqual(self.user.dob, dob)

    def test_dislplay_dob(self):
        self.assertEqual(self.user.display_email, False)

    def test_display_email(self):
        self.assertEqual(self.user.display_email, False)

    def test_allow_messages(self):
        self.assertEqual(self.user.allow_messages, True)

    def test_allow_friend_request(self):
        self.assertEqual(self.user.allow_friend_request, True)

    def test_email_notifications(self):
        self.assertEqual(self.user.email_notifications, False)

    def test_null_password_reset_token(self):
        self.assertEqual(self.user.password_reset_token, None)

    def test_password_reset_token(self):
        self.user.password_reset_token = token
        self.assertEqual(self.user.password_reset_token, token)
