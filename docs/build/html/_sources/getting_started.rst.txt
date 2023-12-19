Uruchamianie Aplikacji
======================

Wymagania Wstępne
-----------------

Upewnij się, że masz zainstalowany Python w wersji co najmniej 3.8 oraz menedżer pakietów pip. Dodatkowo, zalecamy korzystanie z narzędzia do zarządzania wirtualnymi środowiskami, takiego jak `virtualenv`.

Instalacja
----------

1. **Klonowanie Repozytorium**:
   
   Sklonuj repozytorium aplikacji na swój lokalny komputer za pomocą Git:
   
   .. code-block:: bash

       git clone https://github.com/PZZ-US/PZZ.git
       cd PZZ

2. **Tworzenie i Aktywacja Wirtualnego Środowiska `djangoenv`**:
   
   W katalogu projektu utwórz wirtualne środowisko o nazwie `djangoenv` i aktywuj je:

   .. code-block:: bash

       python -m venv djangoenv
       source djangoenv/bin/activate  # Na systemach Unix/Linux
       djangoenv\Scripts\activate  # Na Windows

3. **Instalacja Zależności**:

   Zainstaluj wszystkie wymagane zależności za pomocą pip:

   .. code-block:: bash

       pip install -r requirements.txt

Konfiguracja
------------

4. **Konfiguracja Bazy Danych**:

   Upewnij się, że plik `settings.py` Twojej aplikacji Django zawiera poprawne ustawienia dla Twojej bazy danych.

5. **Migracje Bazy Danych**:

   Przeprowadź migracje, aby przygotować strukturę bazy danych:

   .. code-block:: bash

       python manage.py migrate

Uruchomienie
------------

6. **Uruchomienie Serwera Rozwojowego**:

   Uruchom lokalny serwer rozwojowy:

   .. code-block:: bash

       python manage.py runserver

   Teraz aplikacja powinna być dostępna pod adresem `http://localhost:8000`.

7. **Odwiedzenie Aplikacji w Przeglądarce**:

   Otwórz przeglądarkę internetową i przejdź do `http://localhost:8000` aby zobaczyć działającą aplikację.
