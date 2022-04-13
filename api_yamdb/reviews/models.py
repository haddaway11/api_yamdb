from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

CHOICE_ROLE = (
    (USER, 'аутентифицированный пользователь'),
    (MODERATOR, 'модератор'),
    (ADMIN, 'администратор'),
)

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.TextField(
        'Пользовательская роль',
        max_length=40,
        choices=CHOICE_ROLE,
        default='user',
        blank=True,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=150,
        null=True,
        blank=False,
    )
    
    def is_admin(self):
        return self.role == ADMIN

    def is_moderator(self):
        return self.role == MODERATOR

    def is_user(self):
        return self.role == USER

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='Genre', blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='Category', blank=True, null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    pass


class Comment(models.Model):
    pass

