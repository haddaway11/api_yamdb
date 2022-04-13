from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from reviews.models import User, Category, Genre, Title, Review, Comment




class APIToken(APIView):
    pass


class APISignup(APIView):
    pass


class UserViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass

