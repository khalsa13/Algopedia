from django.contrib import admin
from .models import Post


class PostsView(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostsView)