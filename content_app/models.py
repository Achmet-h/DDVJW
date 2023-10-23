from django.db import models


class ContentType(models.TextChoices):
    article = 'article', 'article'
    podcast = 'podcast', 'podcast'
    blog = 'blog', 'blog'


class Content(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    isPremium = models.BooleanField()
    contentType = models.CharField(max_length=254, choices=ContentType.choices)

    def Search(self):
        return Content.objects.filter(title__contains=self)

    def __str__(self):
        return self.title

