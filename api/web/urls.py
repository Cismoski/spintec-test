from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from web import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
