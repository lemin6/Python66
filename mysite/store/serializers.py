from rest_framework import serializers
from .models import *



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'product_name', 'description', 'category', 'price', 'date', 'active']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'