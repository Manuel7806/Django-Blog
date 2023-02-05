from django.test import TestCase
from user.models import User, UserInfo

# Model Tests


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

    def test_get_user_info(self):
        self.assertEqual(str(self.info), 'johndoe656')

    def test_get_dob(self):
        self.assertEqual(self.info.dob, '1990-10-5')

    def test_get_sex(self):
        self.assertEqual(self.info.sex, 'Male')

    def test_display_email(self):
        self.assertEqual(self.info.display_email, False)

    def test_display_social_media(self):
        self.assertEqual(self.info.display_social_media, False)

    def test_display_sex(self):
        self.assertEqual(self.info.display_sex, False)

    def test_display_dob(self):
        self.assertEqual(self.info.display_dob, False)

    def test_display_active(self):
        self.assertEqual(self.info.display_active, True)

    def test_email_notifications(self):
        self.assertEqual(self.info.get_email_notifications, False)

    def test_allow_friend_request(self):
        self.assertEqual(self.info.allow_friend_request, True)

    def test_allow_messages(self):
        self.assertEqual(self.info.allow_messages, True)