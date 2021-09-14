from rest_framework import viewsets, status
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
import json
import random
from .models import *
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes = [AllowAny, ]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializers(many=True)
    permission_classes = [AllowAny, ]

    def random_string():
        return str(random.randint(100, 2000))

    @action(detail=True, methods=['post'])
    def rate_question(self, request,pk=None):
        if 'data' in request.data:
            list = request.data['data']
            print(list)
            session = Session.objects.create(u_id=random_string())
            list1 = json.dumps(list)
            for data in list:
                print(data['question'], data['answer'])

                answer = Answers.objects.filter(question_id = data['question'], session_id=session.id)
                if len(answer) > 0:
                    answer[0].answer = data['answer'],
                    answer[0].save()
                else:
                    answer = Answers.objects.create(question=Question(data['question']), answer=data['answer'], session=session)
                    answer.save()
                
            return Response(status=status.HTTP_200_OK)
        else:
            response = {'message': 'We need to provide'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
