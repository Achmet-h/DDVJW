from django.db import models


class ContentType(models.Model):
    # Fields for ContentType model
    title = models.CharField(max_length=255)
    description = models.TextField()
    searchable = models.BooleanField()


class Content(models.Model):
    # Fields for Content model
    title = models.CharField(max_length=255)
    description = models.TextField()
    searchable = models.BooleanField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)


class Subscription(models.Model):
    # Fields for Subscription model
    subscription_type = models.CharField(max_length=255)
    subscription_duration = models.CharField(max_length=255)
    subscription_cost = models.FloatField()


class User(models.Model):
    # Fields for User model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    accessed_content = models.ManyToManyField(Content, blank=True)


class Teacher(User):
    # Additional methods or fields for Teacher can be added here
    pass


class Trainer(User):
    # Additional methods or fields for Trainer can be added here
    pass

