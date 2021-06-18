from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)

class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Комментарии'
    author = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.author