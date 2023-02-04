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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
