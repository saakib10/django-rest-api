from rest_framework import serializers

from .models import *

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('name', 'address','image')


class BlogSerializer(serializers.ModelSerializer):
   class Meta:
       model = Blog
       fields = ('author', 'headline', 'context')