from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostListSerializer, CommentItemSerializer, CreateCommentSerializer, CreatePostSerializer, \
    CreateUser, CreateLike
from .models import Post, Comment, Like


# Create ygitour views here.


class GetCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class = PostListSerializer
        else:
            self.serializer_class = CreatePostSerializer
        return self.serializer_class


@api_view(['GET'])
def post_item_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise NotFound('А хуй тебе :)')
    data = PostListSerializer(post).data
    return Response(data=data)


@api_view(['GET'])
def comment_item_view(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        raise NotFound('Такого пиздежа нету :(')
    data = CommentItemSerializer(comment).data
    return Response(data=data)


class CreateComment(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer


class Register(CreateAPIView):
    queryset = User.objects.filter()
    serializer_class = CreateUser

    def post(self, request, *args, **kwargs):
        print(request.data)

        username, password, email = request.data["username"], request.data["password"], request.data["email"]
        user = User.objects.create(username=username, email=email)
        user.set_password(raw_password=password)
        return user


class GetCreateClass(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = CreateLike


class Login(APIView):

    def get(self, request, *args, **kwargs):
        data = request.query_params
        username = data['username']
        password = data['password']
        user = User.objects.filter(username=username, password=password)
        print(user)

        return Response(data={
            "message": 'okay'
        })
