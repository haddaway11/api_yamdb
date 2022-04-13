from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets
from reviews.models import User, Category, Genre, Title, Review, Comment
from django.core.mail import send_mail
from .permissions import IsAdminOrReadOnly
from .serializers import (SignUpSerializer, TokenSerializer,
                          UserSerializer, TitleSerializer,
                          NoStaffSerializer, CategorySerializer,
                          GenreSerializer, ReviewSerializer,
                          CommentSerializer)


class APIToken(APIView):
    pass


class APISignup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Тема письма',
                'Текст письма.',
                'from@example.com',  # Это поле "От кого"
                ['to@example.com'],  # Это поле "Кому" (можно указать список адресов)
                fail_silently=False, # Сообщать об ошибках («молчать ли об ошибках?»)
            ) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = ()
    # filter_backends = ()
    # search_fields = ('username', )

    
    # return Response(serializer.data)
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly,
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly,
    ]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass

