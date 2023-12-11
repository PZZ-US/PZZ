from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    choices = models.TextField() #tutaj podajemy wszystkie możliwe odpowiedzi oddzielone średnikiem
    correct_answer = models.CharField(max_length=255) 

    def __str__(self):
        return self.question
    
class Flashcard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='flashcards')
    sentence = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.sentence
    
class UserProgress(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('quiz', 'Quiz'),
        ('flashcard', 'Flashcard'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES)
    progress = models.FloatField(default=0.0)  

    class Meta:
        unique_together = ('user', 'category', 'category_type')
