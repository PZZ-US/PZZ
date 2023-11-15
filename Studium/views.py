from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Category, Flashcard


def simplehttp(response):
    return HttpResponse("<h1>HI user </h1>")

def home(request):
     return render(request, 'index.html')

def room(request):
    return HttpResponse("Quiz")

def quizzes(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'quizzes.html', context)

def quiz(request):
    return render(request, 'quiz.html')

def flashcards(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'flashcards.html', context)

def flashcard(request):
    return render(request, 'flashcard.html') 

def learning_choice(request):
    return render(request, 'learning_choice.html')

def my_progress(request):
    return render(request, 'my_progress.html')

def my_result(request):
    return render(request, 'my_result.html')

def quizzes_view(request):
    categories = Category.objects.all()
    category_progress = {category.name: 20 for category in categories}
    category_completed = {category.name: True for category in categories}

    context = {
        'categories': categories,
        'category_progress': category_progress,
        'category_completed': category_completed,
    }

    return render(request, 'quizzes.html', context)


def quiz_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    quiz_questions = Quiz.objects.filter(category=category)
    formatted_questions = []

    for question in quiz_questions:
        choices = question.choices.split(';')
        formatted_questions.append({'question': question, 'choices': choices})

    context = {
        'category_name': category_name,
        'progress': 60,
        'quiz_questions': formatted_questions,
    }

    return render(request, 'quiz.html', context)


from django.shortcuts import render
from .models import Flashcard, Category

def flashcard_view(request):
    selected_category_name = request.GET.get('selected_category')

    if selected_category_name:
        selected_category = Category.objects.get(name=selected_category_name)
        flashcards = Flashcard.objects.filter(category=selected_category)
    else:
        flashcards = Flashcard.objects.all()

    return render(request, 'flashcard.html', {'flashcards': flashcards, 'selected_category': selected_category_name})






