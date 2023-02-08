from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    display_email = models.BooleanField(default=False)
    display_dob = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=False)
    allow_friend_request = models.BooleanField(default=True)
    allow_messages = models.BooleanField(default=True)
    password_reset_token = models.CharField(
        max_length=255, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username
