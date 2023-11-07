from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('quiz/', views.quiz, name='quiz'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('flashcard/', views.flashcard, name='flashcard'),
    path('choose-learning/', views.learning_choice, name='learning-choice'),
    path('my-progress/', views.my_progress, name='my-progress'),
    path('my-result/', views.my_result, name='my-result'),
]