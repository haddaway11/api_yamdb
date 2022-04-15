from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from reviews.models import User, Category, Genre, Title, Review, Comment



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.SlugField()
    confirmation_code = serializers.SlugField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'username')

    def validate(self, value):
        if value['username'] == 'me':
            raise serializers.ValidationError('Имя пользователя не может быть "me"!')
        return value


class NoStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    pass


class TitleSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
    pass

