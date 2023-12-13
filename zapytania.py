import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth.models import User
print("Użytkownicy:")
for user in User.objects.all():
    print(user)
print("__________________________________________________\n")


from Studium.models import Category 
print("Kategorie:")
for category in Category.objects.all():
    print(category)
print("__________________________________________________\n")

from Studium.models import Flashcard 
print("Fiszki:")
for flashcard in Flashcard.objects.all():
    print(flashcard)
print("__________________________________________________\n")


from Studium.models import Quiz 
print("Quizy:")
for quiz in Quiz.objects.all():
    print(quiz)
print("__________________________________________________\n")

from Studium.models import Flashcard 
fiszki = Flashcard.objects.filter(sentence='Normalizacja')
for fiszka in fiszki:
    print(f"Kategoria: {fiszka.category.name},\nDefinicja: {fiszka.sentence}, \nOdpowiedź: {fiszka.answer}")



