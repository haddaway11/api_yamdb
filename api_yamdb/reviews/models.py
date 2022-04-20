from django.db import models
<<<<<<< HEAD


USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

CHOICE_ROLE = (
    (USER, 'user'),
    (MODERATOR, 'moderator'),
    (ADMIN, 'admin'),
)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True,
    )
    username = models.SlugField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
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

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_user(self):
        return self.role == USER

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username
=======
from users.models import User
>>>>>>> master


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(default=None, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="titles",
        blank=True, null=True
    )
    genre = models.ManyToManyField(
        Genre, related_name="titles", blank=True
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Review(models.Model):

    SCORE_CHOICES = zip(range(1, 11), range(1, 11))

    score = models.IntegerField(choices=SCORE_CHOICES)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='titles',
    )
    pub_date = models.DateTimeField('Дата публикации ревью', auto_now_add=True)

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='title_author'
            )
        ]


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария', null=True, auto_now_add=True
    )

    class Meta:
        ordering = ['-id']
