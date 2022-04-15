from email import message
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, status, viewsets
from rest_framework.filters import SearchFilter
from reviews.models import User, Category, Genre, Title, Review, Comment
from django.core.mail import send_mail
from .serializers import (SignUpSerializer, TokenSerializer,
                          UserSerializer, TitleSerializer,
                          NoStaffSerializer, CategorySerializer,
                          GenreSerializer, ReviewSerializer,
                          CommentSerializer)
from .permissions import (IsAdmin, IsModerator, IsOwnerOrReadOnly)


class APIToken(APIView):
    """Неавторизованный пользователь отправляет запрос с параметрами username и confirmation_code и получает в ответ токен."""
    
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            username=serializer.validated_data.get('username'),)
        # user = serializer.save()
        if default_token_generator.check_token(
            user, serializer.validated_data.get('confirmation_code'),):
            token = AccessToken.for_user(user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)


class APISignup(APIView):
    """Неавторизованный пользователь отправляет запрос с параметрами e-mail и username и получает в ответ код подтверждения."""
    
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = get_object_or_404(
        #     User,
        #     username=serializer.validated_data.get('username'),)
        # serializer.save()
        user = serializer.save()
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject='Тема письма',
            message=f'Код подтверждения: {confirmation_code}',
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    lookup_field = 'username'
    search_fields = ('username',)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=(IsAuthenticated,),
        url_path='me')
    def private_profile(self, request):
        serializer = UserSerializer(request.user)
        if request.method == 'PATCH':
            if request.user.is_admin:
                serializer = UserSerializer(
                    request.user,
                    data=request.data,
                    partial=True)
            else:
                serializer = NoStaffSerializer(
                    request.user,
                    data=request.data,
                    partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)


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

