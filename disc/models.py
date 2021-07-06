from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)

    def comment_count(self):
        return self.comments.count()


class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Комментарии'

    author = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.author


class Like(models.Model):
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    like = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
