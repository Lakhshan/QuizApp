from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question_text

class UserQuizSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

