from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, UserQuizSession

def start_quiz(request):
    # Create a new quiz session
    session = UserQuizSession.objects.create()
    return JsonResponse({'message': 'New quiz session started', 'session_id': session.session_id})

def get_question(request, session_id):
    # Fetch a random question
    session = UserQuizSession.objects.get(pk=session_id)
    question = random.choice(Question.objects.all())
    return JsonResponse({
        'question_id': question.id,
        'question_text': question.question_text,
        'options': {
            'A': question.option_a,
            'B': question.option_b,
            'C': question.option_c,
            'D': question.option_d,
        }
    })

def submit_answer(request, session_id):
    session = UserQuizSession.objects.get(pk=session_id)
    question_id = request.GET.get('question_id')
    selected_option = request.GET.get('selected_option')

    question = Question.objects.get(pk=question_id)
    session.total_questions += 1
    if selected_option == question.correct_option:
        session.correct_answers += 1
    else:
        session.incorrect_answers += 1
    session.save()

    return JsonResponse({'message': 'Answer submitted'})

def get_score(request, session_id):
    session = UserQuizSession.objects.get(pk=session_id)
    return JsonResponse({
        'total_questions': session.total_questions,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers,
    })
