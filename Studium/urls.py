from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import register

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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('register/', register, name='register'),
]
