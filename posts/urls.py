from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, UpdatePostUpvotesView


router = SimpleRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [path("posts/<int:pk>/upvote", UpdatePostUpvotesView.as_view())]

urlpatterns += router.urls
