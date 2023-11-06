from django.shortcuts import render
from django.http import HttpResponse

def simplehttp(response):
    return HttpResponse("<h1>HI user </h1>")

def home(request):
     return render(request, 'index.html')

def room(request):
    return HttpResponse("Quiz")


def quizzes(request):
    return render(request, 'quizzes.html')

def quiz(request):
    return render(request, 'quiz.html')

def flashcards(request):
    return render(request, 'flashcards.html') 

def flashcard(request):
    return render(request, 'flashcard.html') 

def learning_choice(request):
    return render(request, 'learning_choice.html')

def my_progress(request):
    return render(request, 'my_progress.html')

def my_result(request):
    return render(request, 'my_result.html')