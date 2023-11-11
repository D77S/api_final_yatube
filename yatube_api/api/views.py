from rest_framework import viewsets
#  from django.shortcuts import get_object_or_404

from posts.models import Group  # , Comment, Post
#  from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer  # , CommentSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для групп постов.
    Наследовались специально от ReadOnly,
    чтобы через api нельзя было создать новую группу.
    А только через админку можно было бы.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
