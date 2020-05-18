from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializer import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(requset):
    return Response("hello KKam")


@api_view(['GET'])
def randomQuiz(requset, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)

    return Response(serializer.data)
