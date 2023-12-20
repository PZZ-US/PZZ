from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLoginView, flashcard_view, register

urlpatterns = [
    path('', views.home, name="home"),
    
    path('update-flashcard-and-progress/', views.update_flashcard_and_progress, name='update_flashcard_and_progress'),
    path('update-quiz-and-progress/', views.update_quiz_and_progress, name='update_quiz_and_progress'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('quiz/', views.quiz, name='quiz'),
    path('my-result/', views.my_result, name='my-result'),
    path('quiz/<str:category_name>/', views.quiz_view, name='quiz_view'),

    
    path('flashcards/', views.flashcards, name='flashcards'),
    path('flashcard/', views.flashcard, name='flashcard'), 
    path('flashcards/<str:category_name>/', flashcard_view, name='flashcard_view'),

    
    path('choose-learning/', views.learning_choice, name='learning-choice'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', register, name='register'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('progress-block/', views.progress_block, name='progress-block'),
]
