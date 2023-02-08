from django.test import TestCase
from blog.models import Post, Comments
from user.models import User
import datetime


class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe',
                                        username='johndoe555', email='johndoe@site.com', password='password')
        self.post = Post.objects.create(title='Test Post', body='This is the body!!!',
                                        date_posted=datetime.date.today(), slug='Test-post', user=self.user)

    def test_post(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_instance(self):
        self.assertIsInstance(self.post, Post)

    def test_get_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_get_body(self):
        self.assertEqual(self.post.body, 'This is the body!!!')

    def test_get_date_posted(self):
        self.assertEqual(self.post.date_posted, datetime.date.today())

    def test_get_user(self):
        self.assertEqual(str(self.post.user), str(self.user))
