from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils.html import json_script
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .forms import CustomLoginForm, CustomRegisterForm
from .models import Quiz, Category, Flashcard, UserProgress, UserFlashcardProgress

def home(request):
    return render(request, 'index.html')

def learning_choice(request):
    return render(request, 'learning_choice.html')



def update_flashcard_and_progress(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        flashcard_id = data.get('flashcardId')
        remembered = data.get('remembered')
        category_name = data.get('categoryName')
        new_progress = data.get('progress')

        category = Category.objects.get(name=category_name)
        user_flashcard_progress, created = UserFlashcardProgress.objects.update_or_create(
            user=request.user, 
            flashcard_id=flashcard_id,
            defaults={'remembered': remembered}
        )
        
        user_progress, created = UserProgress.objects.update_or_create(
            user=request.user, 
            category=category, 
            category_type='flashcard',
            defaults={'progress': new_progress}
        )

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



# ------------------         QUIZ       ------------------------

@login_required(redirect_field_name='next')
def quiz(request):
    return render(request, 'quiz.html')

@login_required(redirect_field_name='next')
def quizzes(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'quizzes.html', context)

@login_required(redirect_field_name='next')
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

@login_required(redirect_field_name='next')
def quiz_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    quiz_questions = Quiz.objects.filter(category=category)
    formatted_questions = []

    for question in quiz_questions:
        choices = question.choices.split(';')
        formatted_questions.append({'question': question, 'choices': choices})
        print(question)
        print(choices)

    context = {
        'category_name': category_name,
        'progress': 60,
        'quiz_questions': formatted_questions,
        'questions': quiz_questions,
    }

    return render(request, 'quiz.html', context)


# ------------------         FLASHCARD       ------------------------

@login_required(redirect_field_name='next')
def flashcards(request):
    categories = Category.objects.annotate(num_flashcards=Count('flashcards')).filter(num_flashcards__gt=1)

    for category in categories:
        user_progress = UserProgress.objects.filter(user=request.user, category=category, category_type='flashcard').first()
        category.user_progress = user_progress.progress if user_progress else 0

    return render(request, 'flashcards.html', {'categories': categories})

@login_required(redirect_field_name='next')
def flashcard(request):
    return render(request, 'flashcard.html')

@login_required(redirect_field_name='next')
def flashcard_view(request, category_name):
    category = Category.objects.get(name=category_name)
    flashcards = Flashcard.objects.filter(category=category)
    
    flashcards_data = []
    for flashcard in flashcards:
        user_flashcard_progress = UserFlashcardProgress.objects.filter(
            user=request.user, flashcard=flashcard
        ).first()

        remembered = user_flashcard_progress.remembered if user_flashcard_progress else False
        flashcards_data.append({
            'id': flashcard.id,
            'sentence': flashcard.sentence,
            'answer': flashcard.answer,
            'remembered': remembered
        })

    flashcards_json = mark_safe(json.dumps(flashcards_data))
    
    user_progress, created = UserProgress.objects.get_or_create(
        user=request.user, 
        category=category,
        category_type='flashcard',
        defaults={'progress': 0}
    )
    
    context = {
        'selected_category': category.name,
        'flashcards': flashcards,
        'flashcards_json': flashcards_json,
        'user_progress': round(user_progress.progress)
    }
    
    return render(request, 'flashcard.html', context)


# ------------------         LOGIN       ------------------------

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
    
def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Konto zostało utworzone, zaloguj się.')
            user = form.save()
            return redirect('login')  
        else:
            print(form.errors)
            messages.error(request, 'Wystąpił błąd podczas tworzenia konta.')
    else:
        form = CustomRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# ------------------         DASHBOARD       ------------------------


@login_required(redirect_field_name='next')
def dashboard(request):
    return render(request, 'dashboard.html') 

@login_required(redirect_field_name='next')
def progress_block(request):
    user_progresses = UserProgress.objects.filter(user=request.user, progress__gt=0)
    context = {
        'user_progresses': user_progresses,
    }
    return render(request, 'progress_block.html', context)


@login_required(redirect_field_name='next')
def my_result(request):
    return render(request, 'my_result.html')
