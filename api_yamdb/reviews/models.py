from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404


class Review(models.Model):

    SCORE_CHOICES = zip(range(1, 11), range(1, 11))

    score = models.IntegerField(choices=SCORE_CHOICES)
    title_id = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='titles'
    )
    pub_date = models.DateTimeField('Дата публикации ревью', auto_now_add=True)

    def clean(self):
        title_id = self.title_id_id
        title = get_object_or_404(Title, pk=title_id)
        reviews = title.reviews.all()
        list_res = reviews.filter(author=self.author)

        if list_res:
            raise ValidationError('Нельзя оставить второй отзыв!')


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария', auto_now_add=True
    )
