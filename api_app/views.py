from rest_framework import viewsets
from django.shortcuts import render
from .serializers import BlogSerializer,AuthorSerializer
from .models import Blog,Author


class AuthorViewSet(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
   
   
def apiview(request):
   return render(request,"api.html")