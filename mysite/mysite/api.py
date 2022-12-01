from rest_framework import routers

from polls.views import QuestionChoicesViewSet, QuestionViewSet, ChoiceViewSet
router = routers.DefaultRouter()
router.register('polls/questions', QuestionViewSet,basename='questions')
router.register('polls/choices', ChoiceViewSet,basename='choices')
router.register('polls/questionchoices', QuestionChoicesViewSet,basename='questionchoices')