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
 > Do zrobienia: 
<img width="689" height="520" alt="image" src="https://github.com/user-attachments/assets/66c723b1-398b-4985-886f-82a9eb2f9531" />

To tak brakuje zapytań, nimi się nie zajmowałam zbytnio, I mean są te takie bazowe w tym pliku views.py (stąd są zapytania na API, i to jest wtedy ta 3 kropki - zapytania purely przez backend, na razie dodałam tylko przykładowe 4 postacie, jest też implementacja teamu, oraz slotów (nie wiem czy działa, pewnie czegoś brakuje, nie siedziałam nad tym), próbowałam tą baze danych importować jako plik .bd i wtedy otwiertać przez aplikacje i tam można te zapytania robić, ale kurwa nie współpracuje kompletnie te .db, jak ty umiesz to ogarnąć to śmiało. No i trzeba dokończyć dodawanie użytkownika (nazwa + hasło hashowane). 
 
 > [!IMPORTANT]
 > Dodatkowe informacje:
 
Nie wiem jak to działa w VS Code, ale i tak Ci napisze rzeczy które musiałam dodać żeby działało/ co używałam itp

1. Flask - to jest ogólnie połączone z tych SQLAlchemy, ja to pobierałam jako pip install flask flask_sqlalchemy (z menu "Python Environments");
2. venv (env) - środowisko pythonowe w którym jest to robione, mi to automatycznie VS pobrał otwierając ten projekt przez Flaskowy Web Projekt, ale ty będziesz to musiał sam ogarnąć;
3. Debug - musiałam w Debug Properties projektu dodać Working Directory bo nie było, ale ogólnie żeby Ci generowało plik bazy (.dp w instance) to musi to wyglądać tak:
    - startup file: BD_Backend\runserver.py
    - working directory: BD_Backend
4. On chce mieć jakiś podgląd do tej bazy nie, i on dał jakieś propozycje programów ale ja pobrałam po prostu "DB Broswer for SQLite"
5. Teraz pracuje żeby ta .db była ciągle updatetowana, bo like szczerze MAM DOŚĆ, MAM OCHOTE WYDŁUBAĆ SOBIE OCZY ŻEBY NIE MUSIEĆ NA TO DŁUŻEJ PATRZEĆ, NIE WIEM CO JEST ŹLE ALE DANE NIE CHCĄ SIĘ ZAPISYWAĆ DO TEJ ZASRANEJ BAZY, PRZYNAJMNIEJ W KOŃCU DO NICH PODGLĄD PRZEZ API ALE BOŻE, DAJ MI SIŁE BO JA JUŻ NIE MOGĘ. Anyway jak chcesz sobie odpisalić localhosta i polookać co tam się dzieje na polu bitwy to http://127.0.0.1:5000/api/ [tu wpisujesz co chcesz zobaczyć]
6. Ostatecznie działa, ale że aktualnie to są testy to baza danych jest czyszczona za każdym razem, więc seed leci na nowej, ale ostatecznie działa, nwm jeszcze jak obsłużyć zapytania sql bo plik .db ignoruje dane w tabelkach ale no, jest coś.

 
