from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Group, Post


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
        read_only_fields = (
            'author',
            'post',
            'created'
        )


class CommentSerializer(serializers.ModelSerializer):
    '''Класс сериализатора каментов к постам.'''
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
