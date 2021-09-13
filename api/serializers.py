from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        def create(self,validate_data):
            user = User.objects.create_user(**validate_data)
            return user


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','title','count','q_type','s_no']


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id','question','answer','session']
        