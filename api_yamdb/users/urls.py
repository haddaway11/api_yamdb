from django.urls import include, path
from rest_framework import routers

from .views import (APIToken, APISignup, UserViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', APIToken.as_view(), name='token'),
    path('v1/', include(router.urls)),
]
