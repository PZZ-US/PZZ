import json
from django.core.management.base import BaseCommand
from Studium.models import Flashcard, Quiz, Category

class Command(BaseCommand):
    help = 'Uruchom, aby wstawić dane do bazy'

    def handle(self, *args, **kwargs):
        flashcard_json_files = {
            "Architektura komputerów": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\akflash.json',
            "Systemy operacyjne i programowanie systemowe": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\sopsflash.json',
            "Sieci komputerowe": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\sieciflash.json',
            "Algorytmy i struktury danych": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\aisdflash.json',
            "Programowanie": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\programowanieflash.json',
            "Bazy danych": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\bdflash.json',
            "Elementy grafiki komputerowej": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\grafikaflash.json',
            "Podstawy sztucznej inteligencji": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_fiszka\psiflash.json',
        }

        quiz_json_files = {
            "Architektura komputerów": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\akquiz.json',
            "Systemy operacyjne i programowanie systemowe": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\systemyquiz.json',
            "Sieci komputerowe": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\sieciquiz.json',
            "Algorytmy i struktury danych": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\aisdquiz.json',
            "Programowanie": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\programowaniequiz.json',
            "Bazy danych": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\bazyquiz.json',
            "Elementy grafiki komputerowej": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\grafikaquiz.json',
            "Podstawy sztucznej inteligencji": r'C:\Users\piotr\PycharmProjects\PZZ\Studium\data_json\json_quiz\sztucznaquiz.json',
        }

        for category_name, json_file in flashcard_json_files.items():
            category, created = Category.objects.get_or_create(name=category_name)

            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for term, definition in data.items():
                flashcard = Flashcard.objects.create(
                    category=category,
                    sentence=term,
                    answer=definition
                )

        for category_name, json_file in quiz_json_files.items():
            category, created = Category.objects.get_or_create(name=category_name)

            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            for question_data in data:
                question = question_data['question']
                choices = "\n".join(question_data['choices'])
                correct_answer = question_data['correct_answer']

                quiz_question = Quiz.objects.create(
                    category=category,
                    question=question,
                    choices=choices,
                    correct_answer=correct_answer
                )
