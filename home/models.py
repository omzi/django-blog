import os
import random
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(16))
    return 'uploads/{basename}{randomstring}{ext}'.format(basename = basefilename.replace(" ", ""), randomstring = randomstr, ext = file_extension)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image')
    summary = models.CharField(max_length=255, default='')
    body = RichTextField(default='')
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title + ' / ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return f'{self.post.title} - {self.author}'