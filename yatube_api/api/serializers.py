from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Follow, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    '''Класс сериализатора постов.'''
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    '''Класс сериализатора групп постов.'''
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('title',
                            'slug',
                            'description')


class CommentSerializer(serializers.ModelSerializer):
    '''Класс сериализатора каментов к постам.'''
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    '''Класс сериализатора фолловеров.'''
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate_following(self, value):
        '''Валидирует поле "following".
        Сравнивает его с текущим залогиненным юзером
        и если совпадает - вызывает исключение
        и затем далее код ответа 400.
        '''
        if value == self.context['request'].user:
            raise serializers.ValidationError
        ('Сам на себя нельзя подписываться.')
        return value

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
