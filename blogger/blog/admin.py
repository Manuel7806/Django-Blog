from django.contrib import admin
from .models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'slug', 'user')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
