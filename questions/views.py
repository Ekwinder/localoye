from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Category
from .serializers import QuestionSerializer, CategorySerializer
# Create your views here.

@api_view(['GET'])
def question_list(request):
    """
    List all questions.
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    """
    List all categories.
    """
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def question_category_list(request, category):
    """
    List all questions bases on categories.
    """
    if request.method == 'GET':
    	try:
        	questions = Question.objects.filter(category__name__icontains=category)
        except Question.DoesNotExist:
        	return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def question_add(request):
    """
    add a question
    """
    if request.method == 'POST':
	    serializer = QuestionSerializer(data=request.DATA)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    else:
	        return Response(
	            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAdminUser,))
def question_detail(request, pk):
    """
    Get, update, or delete a specific question
    """
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)