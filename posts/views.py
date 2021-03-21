from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, CommentSerializer, PostUpvotesSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author_name=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author_name=self.request.user)


class UpdatePostUpvotesView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpvotesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (JWTAuthentication,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user,
                        upvoted=self.request.data["upvoted"])
