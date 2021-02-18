from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
user = get_user_model()


class Upvote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(user, related_name="upvotes", on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name="upvotes", on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username

    class Meta:
        ordering = ["created"]


    def Check(self, post, owner):
        if self.objects.get(owner=owner, post=post):
            return True
        else:
            return False


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    link = models.URLField(max_length=254, blank=False, unique=True)
    owner = models.ForeignKey(user, related_name="posts", on_delete=models.CASCADE)

    @property
    def upvotesNum(self):
        return self.upvotes.all().count()


    @property
    def commentsNum(self):
        return self.comments.all().count()

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(user, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username

    class Meta:
        ordering = ["created"]