from dataclasses import fields
from pyexpat import model
import re
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','author','email']