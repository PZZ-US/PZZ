from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    """
    Reprezentuje kategorię w systemie.

    Atrybuty:
        name (models.CharField): Nazwa kategorii.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        """
        Zwraca reprezentację tekstową kategorii.

        Returns:
            str: Nazwa kategorii.
        """
        return self.name
    
class Quiz(models.Model):
    """
    Definiuje model Quiz, który zawiera pytania i odpowiedzi.

    Atrybuty:
        category (models.ForeignKey): Kategoria, do której należy quiz.
        question (models.TextField): Treść pytania.
        choices (models.TextField): Dostępne opcje odpowiedzi.
        correct_answer (models.CharField): Poprawna odpowiedź na pytanie.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    choices = models.TextField()
    correct_answer = models.CharField(max_length=255) 

    def __str__(self):
        """
        Zwraca treść pytania quizu.

        Returns:
            str: Treść pytania.
        """
        return self.question
    
class Flashcard(models.Model):
    """
    Model reprezentujący fiszkę do nauki.

    Atrybuty:
        category (models.ForeignKey): Kategoria, do której należy fiszka.
        sentence (models.CharField): Zdanie lub pytanie na fiszce.
        answer (models.TextField): Odpowiedź do zdania lub pytania.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='flashcards')
    sentence = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        """
        Zwraca zdanie lub pytanie z fiszki.

        Returns:
            str: Zdanie lub pytanie.
        """
        return self.sentence
    
class UserProgress(models.Model):
    """
    Model śledzący postęp użytkownika w różnych kategoriach.

    Atrybuty:
        user (models.ForeignKey): Użytkownik, którego dotyczy postęp.
        category (models.ForeignKey): Kategoria, w której śledzony jest postęp.
        category_type (models.CharField): Typ kategorii ('quiz' lub 'flashcard').
        progress (models.FloatField): Procentowy postęp użytkownika w danej kategorii.
    """

    CATEGORY_TYPE_CHOICES = (
        ('quiz', 'Quiz'),
        ('flashcard', 'Flashcard'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES)
    progress = models.FloatField(default=0)  

    class Meta:
        unique_together = ('user', 'category', 'category_type')


class UserFlashcardProgress(models.Model):
    """
    Model reprezentujący postęp użytkownika w nauce za pomocą fiszek.

    Atrybuty:
        user (models.ForeignKey): Użytkownik, którego dotyczy postęp.
        flashcard (models.ForeignKey): Fiszka, której dotyczy postęp.
        remembered (models.BooleanField): Flaga wskazująca, czy użytkownik zapamiętał fiszkę.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    remembered = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'flashcard')
