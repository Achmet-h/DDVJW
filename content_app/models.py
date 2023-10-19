from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, role, telephone=None, school_name=None, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             role=role.CLIENT,
#             telephone=telephone,
#             school_name=school_name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, first_name, last_name, password):
#         return self.create_user(email, first_name, last_name, role=Role.TRAINER, password=password)
#
#     def get_by_natural_key(self, email):
#         return self.get(email=email)
#
#
# class Role(models.TextChoices):
#     TRAINER = 'trainer', 'trainer'
#     CLIENT = 'client', 'client'
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     telephone = models.CharField(max_length=15, blank=True, null=True)
#     school_name = models.CharField(max_length=255, blank=True, null=True)
#     role = models.CharField(max_length=255, choices=Role.choices, default=Role.CLIENT)
#
#     is_active = models.BooleanField(default=True)  # If the user is currently active
#     is_staff = models.BooleanField(default=False)  # If the user can access the Django admin site
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     objects = CustomUserManager()
