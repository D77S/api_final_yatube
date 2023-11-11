from rest_framework import permissions, viewsets
#  from django.shortcuts import get_object_or_404

from posts.models import Group, Post  # , Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, PostSerializer  # , CommentSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для групп постов.
    Наследовались специально от ReadOnly,
    чтобы через api нельзя было создать новую группу.
    А только через админку можно было бы.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.
        При создании поста нам надо, чтобы
        id автора камента брался именно из реквеста
        (даже если какой-то и пришел в словаре api, мы ему не верим).
        '''
        serializer.save(author=self.request.user)
