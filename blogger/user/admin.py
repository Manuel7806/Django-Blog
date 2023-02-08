from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
        'display_email',
        'display_dob',
        'allow_messages',
        'allow_friend_request',
        'email_notifications',
        'password_reset_token'
    )

    prepopulated_fields = {'slug': ('username')}


admin.site.register(User)
