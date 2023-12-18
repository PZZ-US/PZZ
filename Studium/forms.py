from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    """
    Formularz dostosowany do logowania użytkownika.

    Rozszerza standardowy formularz logowania Django, dodając niestandardowe atrybuty
    do pól formularza, aby umożliwić lepszą kontrolę nad ich stylizacją.

    Atrybuty:
        username (forms.CharField): Pole tekstowe dla nazwy użytkownika. Używa widgetu TextInput
                                    z dodatkowymi atrybutami klasy i placeholdera.
        password (forms.CharField): Pole tekstowe dla hasła. Używa widgetu PasswordInput
                                    z dodatkowymi atrybutami klasy i placeholdera.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))

class CustomRegisterForm(UserCreationForm):
    """
    Formularz dostosowany do rejestracji nowego użytkownika.

    Rozszerza standardowy formularz rejestracji Django, dodając pole e-mail i niestandardowe
    atrybuty do pól formularza.

    Atrybuty:
        email (forms.EmailField): Pole e-mail wymagane do rejestracji.

    Meta:
        model (User): Model Django User używany przez formularz.
        fields (list): Lista pól do wyświetlenia w formularzu.
    
    Metody:
        __init__: Konstruktor klasy, który inicjalizuje formularz i dostosowuje atrybuty widgetów.
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Adres e-mail'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def __init__(self, *args, **kwargs):
        """
        Inicjalizuje formularz rejestracyjny, ustawiając niestandardowe placeholdery dla pól.

        Args:
            *args: Argumenty zmienne pozycyjne.
            **kwargs: Argumenty zmienne słownikowe.
        """
        super(CustomRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdź hasło'
