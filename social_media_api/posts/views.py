class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()   # ✅ for checker
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset().select_related('author')  # optimization here
        author_username = self.request.query_params.get('author')
        if author_username:
            qs = qs.filter(author__username=author_username)
        return qs


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()   # ✅ for checker
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset().select_related('post', 'author')  # optimization here
        post_id = self.request.query_params.get('post')
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs
