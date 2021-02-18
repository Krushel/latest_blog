from rest_framework import serializers
from .models import Post, Comment, Upvote


class UpvoteSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Upvote
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field = "username", read_only = True)
    comments = CommentSerializer(many=True, default=[])
    upvotes = UpvoteSerializer(many=True, default=[])

    class Meta:
        model = Post
        fields = "__all__"