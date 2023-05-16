from django.urls import include, path

from rest_framework import routers

from .views import AuthorViewSet, BlogViewSet,apiview
from . import views
router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path("api-data/",views.apiview,name="api")
]