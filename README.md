# BazaDanych
## Backend:
 > [!IMPORTANT]
 > Budowa projektu: 
 
<img width="283" height="450" alt="image" src="https://github.com/user-attachments/assets/1e56e764-b511-4702-abc1-b4dbe6ab4a6e" />

1. **models** - folder z wszystkimi modelami SQLAlchemy opisującymi strukturę bazy danych. Każdy model odpowiada jednej tabeli lub tabeli łączącej w relacje many-to-many.
    - \_\_init\_\_.py - plik inicjujący moduł — pozwala importować modele jako from models import User, Character. Łączy folder models z resztą programu.
2. **static** - folder przeznaczony na pliki statyczne (CSS, JS, obrazy). Przygotowany pod przyszłą pracę z frontendem.
3. **templates** - folder z szablonami HTML, aktualnie jest pusty, stworzony został on z myślą o generowniu widoków serwerowych w przyszłości.
4. **\_\_init\_\_.py** - centrala aplikacji Flask, odpowiada za:
    - stworzenie instancji aplikacji,
    - wczytanie konfiguracji,
    - inicjalizację rozszerzeń (db),
    - rejestrację blueprintów (np. /api).
5. **config.py** - plik konfiguracyjny aplikacji, na tą chwilę przechowuje:
    - ścieżkę bazy danych SQLAlchemy.
6. **extensions.py** - centrane miejsce inicjalizacji rozszerzeń.
7. **requirements.txt** - lista zależności Pythona wymaganych do uruchomienia backendu.
8. **runserver.py** - plik startowuy serwera, odpowiada za:
    - stworzenie/wyczyszczenie bazy,
    - nadanie ścieżki do pliku bazy danych .db,
    - uruchomienie aplikacji Flask w trybie dev (debug=True).
9. **seed.py** - skrypt "seedujący" bazę, działa jednorazowo przy uruchomieniu bazy dodając rekordy startowe:
    - początkowe postacie,
    - efekty,
    - skille itp.
10. **views.py** - główna logika API, zawiera:
    - rejestrację użytkownika / logowanie,
    - CRUD dla postaci,
    - przypisywanie postaci do użytkownika,
    - tworzenie/usuwanie drużyn,
    - listowanie postaci i drużyn użytkownika.

 > [!IMPORTANT]
 > Dodatkowe informacje:
 
 
