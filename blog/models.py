from django.db import models
from django.urls import reverse

class Article(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={'id':self.id})
