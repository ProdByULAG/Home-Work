from rest_framework import serializers
from .models import Post, Comment


class CommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    comments = CommentItemSerializer(many=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = 'title text created comments comments_count'.split()



    def get_comments_count(self, obj):
        return obj.comment_count()
