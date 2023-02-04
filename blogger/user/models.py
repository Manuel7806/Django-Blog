from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class UserInfo(models.Model):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non Binary'),
        ('O', 'Other'),
    )

    dob = models.DateField('Date of Birth')
    sex = models.CharField(max_length=25, choices=genders)
    display_email = models.BooleanField(default=False)
    display_social_media = models.BooleanField(default=False)
    display_sex = models.BooleanField(default=False)
    display_dob = models.BooleanField(default=False)
    display_active = models.BooleanField(default=True)
    get_email_notifications = models.BooleanField(default=False)
    allow_friend_request = models.BooleanField(default=True)
    allow_messages = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def is_active(self) -> bool:
        return self.active

    def __str__(self):
        return self.user.username
