from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField("get_user_count")

    @staticmethod
    def get_user_count(obj):
        return obj.amount_of_upvotes.count()

    class Meta:
        fields = (
            "title",
            "upvote_count",
        )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "post",
            "content",
        )
        model = Comment


class PostUpvotesSerializer(serializers.ModelSerializer):

    upvote_count = serializers.SerializerMethodField("get_user_count")

    @staticmethod
    def get_user_count(obj):
        return obj.amount_of_upvotes.count()

    class Meta:
        fields = ("upvote_count",)
        model = Post

    def save(self, **kwargs):
        self.validated_data["user"] = kwargs["user"]
        self.validated_data["upvoted"] = kwargs["upvoted"]
        self.update(self.instance, self.validated_data)

    def update(self, instance, validated_data):
        cur_user = validated_data.pop("user")
        upvoted = validated_data.pop("upvoted")
        post = Post.objects.get(pk=instance.pk)

        if upvoted:
            post.amount_of_upvotes.add(cur_user)
        else:
            post.amount_of_upvotes.remove(cur_user)
        post.save()
