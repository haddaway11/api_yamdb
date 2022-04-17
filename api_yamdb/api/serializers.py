from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        exclude = ('title_id', )
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        exclude = ('review_id', )
        model = Comment
