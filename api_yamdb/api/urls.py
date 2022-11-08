from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       RegisterUserAPI, ReviewViewSet, TitleViewSet,
                       TokenObtainAPI, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

API_PREFIX = 'v1'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories'),
router.register(r'genres', GenreViewSet, basename='genres'),
router.register(r'titles', TitleViewSet, basename='titles'),
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path(f'{API_PREFIX}/', include(router.urls)),
    path(
        f'{API_PREFIX}/auth/signup/',
        RegisterUserAPI.as_view(),
        name='register_user'),
    path(
        f'{API_PREFIX}/auth/token/',
        TokenObtainAPI.as_view(),
        name='token_obtain'),
]
