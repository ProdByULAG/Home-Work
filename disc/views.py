from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import PostListSerializer, CommentListSerializer
from .models import Post, Comment
# Create ygitour views here.

@api_view(['GET'])
def post_list_view(request):
    posts = Post.objects.all()
    data = PostListSerializer(posts, many=True).data
    return Response(data={'list' : data})



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
    data = CommentListSerializer(comment).data
    return Response(data=data)