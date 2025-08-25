from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    list/create/retrieve/update/destroy for posts
    """
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # search & ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        # set current user as author
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        # optional filter: ?author=<username>
        author_username = self.request.query_params.get('author')
        if author_username:
            qs = qs.filter(author__username=author_username)
        return qs


class CommentViewSet(viewsets.ModelViewSet):
    """
    list/create/retrieve/update/destroy for comments
    """
    queryset = Comment.objects.select_related('post', 'author').all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # enable searching comments by content or author name
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        # filter by post id: ?post=<id>
        post_id = self.request.query_params.get('post')
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

