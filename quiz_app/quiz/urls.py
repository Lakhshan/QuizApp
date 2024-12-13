from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/<int:session_id>/', views.get_question, name='get_question'),
    path('submit/<int:session_id>/', views.submit_answer, name='submit_answer'),
    path('score/<int:session_id>/', views.get_score, name='get_score'),
]
