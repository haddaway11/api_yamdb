from rest_framework import routers
from django.urls import include, path
from .views import (
    UserViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
    ReviewViewSet, CommentViewSet
)


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
