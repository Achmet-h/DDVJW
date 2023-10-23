from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, role, telephone=None, school_name=None, password=None,
                    **other_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            telephone=telephone,
            school_name=school_name,
            is_staff=other_fields.get('is_staff', False),
            is_superuser=other_fields.get('is_superuser', False)
        )

        if role == Role.TRAINER:
            user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(email, first_name, last_name, role=Role.TRAINER, password=password, **other_fields)


class Role(models.TextChoices):
    TRAINER = 'trainer', 'trainer'
    CLIENT = 'client', 'client'


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.CLIENT)

    is_active = models.BooleanField(default=False)  # If the user is currently active, this can also be changed to
    # verify using an email
    is_staff = models.BooleanField(default=False)  # If the user can access the Django admin site

    def __str__(self):
        return self.first_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomAccountManager()
