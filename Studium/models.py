from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    choices = models.TextField() #tutaj podajemy wszystkie możliwe odpowiedzi oddzielone średnikiem
    correct_answer = models.CharField(max_length=255) #a tu jedną poprawną

    def __str__(self):
        return self.question
    
class Flashcard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='flashcards')
    sentence = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.sentence
    
