#  login/pass admin1/admin1
from django.contrib import admin
from posts.models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text', 'pub_date', 'author__username',
                     'group__title', 'image')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug', 'description')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    search_fields = ('user_username', 'following__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author_username', 'post__text',
                     'text', 'created')
