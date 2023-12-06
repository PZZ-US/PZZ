from django.contrib import admin
from .models import Quiz, Question, Answer, FlashcardCategory, Flashcard

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(FlashcardCategory)
admin.site.register(Flashcard)