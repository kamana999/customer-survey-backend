from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

class Question(models.Model):
    STARS = "ST"
    TEXT = "TXT"
    CHOICES = (
        (STARS,"stars"),
        (TEXT, "text")
    )
    title = models.CharField(max_length=200)
    s_no = models.IntegerField()
    q_type = models.CharField(choices=CHOICES, default=STARS, max_length=30)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


def random_string():
    return str(random.randint(1, 20))

class Session(models.Model):
    u_id = models.IntegerField(default = random_string)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=None)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer
    
    class Meta:
        unique_together = (('question', 'session'),)
        index_together = (('question', 'session'),)

