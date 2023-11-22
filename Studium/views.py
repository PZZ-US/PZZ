from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomLoginForm
from .forms import CustomRegisterForm
from django.contrib import messages

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