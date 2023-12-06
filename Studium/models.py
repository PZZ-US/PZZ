from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    number_of_questions = models.IntegerField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    last_result = models.IntegerField(null=True, blank=True)

class FlashcardCategory(models.Model):
    name = models.CharField(max_length=100)

class Flashcard(models.Model):
    category = models.ForeignKey(FlashcardCategory, related_name='flashcards', on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    definition = models.TextField()

class UserFlashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    remembered = models.BooleanField(default=False)
