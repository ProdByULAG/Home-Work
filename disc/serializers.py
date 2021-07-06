from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, Comment, Like


class CommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, attrs):
        if Comment.objects.filter(text=attrs["text"], post=attrs["post"]).count() > 0:
            raise ValidationError('Такой комментарий уже существует')
        elif len(attrs['text']) < 10:
            raise ValidationError('Длина текста меньше 10')
        return attrs


class PostListSerializer(serializers.ModelSerializer):
    comments = CommentItemSerializer(many=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = 'title text created comments comments_count'.split()

    def get_comments_count(self, obj):
        return obj.comment_count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        like = Like.objects.filter(post=instance).first()
        if like:
            data["like"] = like.like
        else:
            data["like"] = False
        return data


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'title text'.split()

    def validate(self, attrs):
        if Post.objects.filter(title=attrs['title']).count() > 0:
            raise ValidationError('Такой пост уже существует')
        elif len(attrs['text']) < 10:
            raise ValidationError('Ваш текст меньше 10')
        return attrs


class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username password email'.split()


class CreateLike(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = 'like user post'.split()
