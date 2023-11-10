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


class Category(models.TextChoices):
    didactiek = 'didactiek', 'didactiek'
    begeleiding = 'begeleiding', 'begeleiding'
    ondersteuning  = 'ondersteuning', 'ondersteuning'

class FAQ(models.Model):
    category = models.CharField(max_length=254, choices=Category.choices)
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question
    def __str__(self):
        return self.answer