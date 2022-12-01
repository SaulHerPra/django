from rest_framework import viewsets
from .models import Choice, Question
from .serializers import ChoiceModelSerializer, QuestionModelSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionModelSerializer
    permission_classes=[]

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset=Choice.objects.all()
    serializer_class=ChoiceModelSerializer
    permission_classes=[]
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def prueba(request):
#    return HttpResponse("Hello, world. You're at the polls prueba.")
