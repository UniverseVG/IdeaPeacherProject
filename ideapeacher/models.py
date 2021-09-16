from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class ideapeacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)


class category(models.Model):
    category = models.CharField(max_length=100)


class idea(models.Model):
    peacher = models.ForeignKey(
        ideapeacher, on_delete=models.CASCADE, default=None)
    post_idea = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
    category = models.ManyToManyField(category)

    pdf = models.FileField(upload_to="book/pdfs", blank=True)

    def __str__(self):
        return self.post_idea

class Public(models.Model):
    comment = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())
    on_post = models.ForeignKey(idea,on_delete=models.CASCADE,default=None)
    by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.comment