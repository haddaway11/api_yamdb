from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.permissions import AuthorModerAdmOrRead
from api.serializers import CommentSerializer, ReviewSerializer
from reviews.models import Review, Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    permission_classes = [AuthorModerAdmOrRead]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        reviews = title.reviews.all()
        return reviews

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        reviews = title.reviews.all()
        list_res = reviews.filter(author=self.request.user)

        if list_res:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        serializer.save(author=self.request.user, title_id_id=title_id)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination

    permission_classes = [AuthorModerAdmOrRead]

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)
        comments = review.comments.all()
        return comments

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get("review_id")
        serializer.save(author=self.request.user, review_id_id=review_id)
