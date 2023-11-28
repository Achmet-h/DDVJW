from django.db import models
from ckeditor.fields import RichTextField


class ContentType(models.TextChoices):
    article = 'article', 'article'
    podcast = 'podcast', 'podcast'
    blog = 'blog', 'blog'


class Content(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = RichTextField()
    publish = models.DateTimeField(auto_now_add=True)
    isPremium = models.BooleanField()
    contentType = models.CharField(max_length=254, choices=ContentType.choices)
    picture = models.ImageField(upload_to='media', blank=True, null=True)  # New field for the picture

    def Search(self):
        return Content.objects.filter(title__contains=self)

    def __str__(self):
        return self.title


class Category(models.TextChoices):
    Didactiek = 'Didactiek', 'Didactiek'
    Begeleiding = 'Begeleiding', 'Begeleiding'
    Ondersteuning = 'Ondersteuning', 'Ondersteuning'


class FAQ(models.Model):
    category = models.CharField(max_length=254, choices=Category.choices)
    question = models.CharField(max_length=250)
    answer = RichTextField()

    def __str__(self):
        return self.question

    def __str__(self):
        return self.answer


