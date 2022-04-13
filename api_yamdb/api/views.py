from rest_framework import permissions, viewsets
from reviews.models import User, Category, Genre, Title, Review, Comment
from .serializers import (
    UserSerializer, CategorySerializer, GenreSerializer, TitleSerializer,
    ReviewSerializer, CommentSerializer
)




class UserViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass

