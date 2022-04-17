from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import (
    APIToken, APISignup,
    UserViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
    ReviewViewSet, CommentViewSet
)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
    basename='Reviews'
)
router.register(
    (
        r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments'
    ), CommentViewSet, basename='Comments'
)

urlpatterns = [
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', APIToken.as_view(), name='token'),
    path('v1/', include(router.urls)),
]
