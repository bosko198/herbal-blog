from django.contrib import admin
from .models import Post, Image, Comment

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline, CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
