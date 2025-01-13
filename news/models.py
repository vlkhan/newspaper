from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    rating_au = models.FloatField(default=0.0)
    us = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='users')

    def update_rating(self):
        self.rating_au = Post.rating * 3 + Comment.rating_com


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    cat = models.ManyToManyField(Category, through='PostCategory')
    name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    news = models.CharField(max_length=2, choices=[(
        'st', 'Статья'), ('nw', 'Новость')], default='nw')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_c = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_com = models.DateTimeField(auto_now_add=True)
    rating_com = models.IntegerField(default=0)

    def like(self):
        self.rating_com += 1
        self.save()

    def dislike(self):
        self.rating_com -= 1
        self.save()
