from re import S
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes = [AllowAny, ]

    @action(detail=True, methods=['POST'])
    def rate_question(self, request, pk):
        if 'answer' in request.data:
            question = Question.objects.get(pk=pk)
            answer = request.data['answer']
            session = Session.objects.get(id=1)
            try:
                rating = Answers.objects.get(session=session, question=question)
                rating.answer = answer
                rating.save()
                serializer = AnswerSerializers(rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Answers.objects.create(session=session, question=question, answer=answer)
                serializer = AnswerSerializers(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'We need to provide'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [AllowAny, ]