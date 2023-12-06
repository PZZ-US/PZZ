from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomLoginForm
from .forms import CustomRegisterForm
from django.contrib import messages
from .models import FlashcardCategory, Flashcard

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

def dashboard(request):
    return render(request, 'dashboard.html')

def progress_block(request):
    return render(request, 'progress_block.html')

    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login_page.html'
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
    return render(request, 'register_page.html', {'form': form})


from .models import FlashcardCategory, Flashcard

def flashcards_view(request):
    categories = FlashcardCategory.objects.all()
    return render(request, 'flashcards.html', {'categories': categories})


def flashcard_detail(request, category_id, flashcard_id):
    category = get_object_or_404(FlashcardCategory, pk=category_id)
    flashcards = category.flashcards.all()
    current_flashcard = get_object_or_404(Flashcard, pk=flashcard_id, category=category)
    next_flashcard = flashcards.filter(id__gt=flashcard_id).first()
    prev_flashcard = flashcards.filter(id__lt=flashcard_id).last()

    context = {
        'category': category,
        'current_flashcard': current_flashcard,
        'next_flashcard': next_flashcard,
        'prev_flashcard': prev_flashcard,
        'flashcard_count': flashcards.count(),
    }
    return render(request, 'flashcard.html', context)