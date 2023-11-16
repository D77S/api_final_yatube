from django.contrib.auth import get_user_model
from django.db import models

MAX_NAME_LENGTH = 200

User = get_user_model()

class Group(models.Model):
    '''Модель групп постов.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    title = models.CharField(max_length=MAX_NAME_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Модель самих постов.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='authors')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['pub_date', 'text']


class Comment(models.Model):
    '''Модель каментов к постам.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text


class Follow(models.Model):
    '''Модель фолловеров. Они же подписанты, подписки.
    (А вот её писали мы сами уже.)
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscriber')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscribed')

    def __str__(self):
        return f'{str(self.user).capitalize()} подписан на {self.following}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
            models.CheckConstraint(
                check=models.Q(user__exact=models.F('{following}')),
                name='user_not_followed_himself'
            )
        ]
