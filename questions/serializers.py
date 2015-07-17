from rest_framework import serializers
from .models import Category, Question

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('id','title','category','date','answer')

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name')