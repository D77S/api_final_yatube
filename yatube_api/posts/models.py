from django.contrib.auth import get_user_model
from django.db import models
# from django.forms import ValidationError

MAX_NAME_LENGTH = 200

User = get_user_model()

class Group(models.Model):
    '''Модель групп постов.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    title = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Заголовок')
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug')
    description = models.TextField(
        verbose_name='Описание')

    class Meta:
        verbose_name = 'объект группы постов'
        verbose_name_plural = 'Группы постов'

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Модель самих постов.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    text = models.TextField(
        verbose_name='Текст поста'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='Автор')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа поста')
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка к посту')

    class Meta:
        ordering = ['pub_date', 'text']
        verbose_name = 'объект поста'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text

class Comment(models.Model):
    '''Модель каментов к постам.
    (Писали не мы, нам её дали в таком виде в т.з.)
    '''
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемый пост')
    text = models.TextField(
        verbose_name='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True)

    class Meta:
        verbose_name = 'объект комментария'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text

class Follow(models.Model):
    '''Модель фолловеров. Они же подписанты, подписки.
    (А вот её писали мы сами уже.)
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Тот, кто на кого-то подписан')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribed',
        verbose_name='Тот, на кого подписаны')

    class Meta:
        verbose_name = 'объект подписки'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user_not_followed_himself'
            )
        ]

    #  def clean(self):
    #      if self.user == self.following:
    #          raise ValidationError('Самому на себя нельзя подписываться')
    def __str__(self):
        return f'{str(self.user).capitalize()} подписан на {self.following}'
