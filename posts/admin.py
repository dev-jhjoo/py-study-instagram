from django.contrib import admin
from posts.models import Post, PostImage, Comment
import admin_thumbnails

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_dislay = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]