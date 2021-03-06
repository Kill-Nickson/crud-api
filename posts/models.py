from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="blogpost_upvotes", blank=True
    )
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
