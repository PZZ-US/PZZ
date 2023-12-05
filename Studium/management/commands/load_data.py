from django.core.management.base import BaseCommand
from Studium.models import Category, Quiz, Flashcard

class Command(BaseCommand):
    help = 'Uruchom, aby wstawić dane do bazy'

    def handle(self, *args, **kwargs):
        ak = Category.objects.create(name='Architektura komputerów')
        sops = Category.objects.create(name='Systemy operacyjne i programowanie systemowe')
        sk = Category.objects.create(name='Sieci komputerowe')
        aip = Category.objects.create(name='Algorytmy i struktury danych')
        prog = Category.objects.create(name='Programowanie')
        bd = Category.objects.create(name='Bazy danych')
        egk = Category.objects.create(name='Elementy grafiki komputerowej')
        psi = Category.objects.create(name='Podstawy sztucznej inteligencji')

        quiz_question1 = Quiz.objects.create(
            category=ak,
            question='Jakie są trzy główne funkcje jednostki kontrolującej w architekturze komputerowej?',
            choices='a) Dekodowanie instrukcji, pobieranie danych, przetwarzanie obliczeń; b) Pobieranie instrukcji, dekodowanie danych, przesyłanie danych; c) Pobieranie instrukcji, dekodowanie instrukcji, wykonanie instrukcji',
            correct_answer='c) Pobieranie instrukcji, dekodowanie instrukcji, wykonanie instrukcji'
        )

        quiz_question2 = Quiz.objects.create(
            category=ak,
            question='Co to jest pamięć cache w architekturze komputerowej?',
            choices='a) Dodatkowa pamięć RAM służąca do przechowywania plików systemowych; b) Szybka pamięć tymczasowa używana do przechowywania często używanych danych; c) Zewnętrzny dysk twardy do przechowywania kopii zapasowych',
            correct_answer='b) Szybka pamięć tymczasowa używana do przechowywania często używanych danych'
        )

        flashcard1 = Flashcard.objects.create(
            category=bd,
            sentence='Normalizacja', answer='Normalizacja to proces organizacji danych w bazie w celu minimalizacji redundancji i zapobiegania anomalii związanych z manipulacją danymi.')

        flashcard2 = Flashcard.objects.create(
            category=bd,
            sentence='Klucz główny a klucz obcy', answer='Klucz główny jednoznacznie identyfikuje rekord w tabeli, podczas gdy klucz obcy tworzy relację między dwiema tabelami, odwołując się do klucza głównego w innej tabeli.')

