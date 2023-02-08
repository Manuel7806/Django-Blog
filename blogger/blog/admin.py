from django.contrib import admin
from .models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug', 'user', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
