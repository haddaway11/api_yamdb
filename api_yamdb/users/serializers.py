from rest_framework import serializers

from .models import User


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
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me"!'
            )
        return value


class NoStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')
        read_only_fields = ('role',)
