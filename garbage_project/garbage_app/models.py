from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):

    image=models.FileField(null=True,blank=True)
    title = models.CharField(max_length=200)
    Description=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    latitude=models.DecimalField(max_digits=10,decimal_places=8,null=True)
    longitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.Description

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})



class Vote(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    voted_by=models.ForeignKey(User,on_delete=models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Garbage_User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    phone_number=models.IntegerField()

