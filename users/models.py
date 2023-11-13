from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Role(models.TextChoices):
    TRAINER = 'trainer', 'Trainer'
    CLIENT = 'client', 'Client'


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, role=Role.CLIENT, telephone=None, school_name=None,
                    password=None,
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
            **other_fields
        )

        # If the role is TRAINER and is_staff is not explicitly set to True, then make them staff
        if role == Role.TRAINER and not other_fields.get('is_staff', False):
            user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('role', Role.TRAINER)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must be assigned to is_active=True")

        return self.create_user(email, first_name, last_name, password=password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.CLIENT)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomAccountManager()

