from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Follow, Group, Post
from .permissions import MethodIsSafeOrUserIsAuthor
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для групп постов.'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    '''Вьюсет для самих постов.'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (MethodIsSafeOrUserIsAuthor,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.'''
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    '''Вьюсет для каментов.'''
    serializer_class = CommentSerializer
    permission_classes = (MethodIsSafeOrUserIsAuthor,)

    def get_queryset(self):
        '''Перегружает кверисет таким образом,
        чтобы он содержал не вообще все каменты,
        а только каменты к одному конкретному посту.
        Номер поста через кварг получаем из урла.
        '''
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()  # type: ignore

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.
        При создании камента нам надо, чтобы:
        - id автора камента брался именно из реквеста
        (даже если какой-то и пришел в словаре api, мы ему не верим);
        - номер пост, к которому создаем камент, берем из урла по регулярке и
        вытаскиваем сей объект поста из базы постов.
        '''
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    '''Вьюсет для фолловеров.'''
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)
    # Единственный из вьюсетов, в котором
    # не переопределяем свой permission в сторону послабления,
    # а используем permission уровня проекта.

    class Meta:
        model = Follow
        fields = '__all__'

    def get_queryset(self):
        '''Задает кверисет сериалайзера так, чтобы
        входили объекты только текущего юзера.
        '''
        current_user = self.request.user
        return current_user.subscriber.all()  # type: ignore

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.
        При создании подписки нам надо, чтобы
        id кто подписывается брался из реквеста.
        '''
        serializer.save(user=self.request.user)
