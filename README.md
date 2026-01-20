# BazaDanych

## Cel projektu:

Celem projektu było stworzenie interaktywnej aplikacji webowej, która składuje postacie użytkownika a następnie oblicza jakie połączenia postaci (teamy) najlepiej pasują pod wybranego przez użytkownika DPS'a.

## Funkcjonalności aplikacji

- Rejestracja i logowanie użytkownika
- Przechowywanie postaci przypisanych do konta użytkownika
- Dodawanie i usuwanie postaci z kolekcji użytkownika
- Tworzenie drużyn (teamów) składających się z maksymalnie 4 postaci
- Edycja oraz usuwanie istniejących drużyn
- Automatyczne obliczanie dopasowania teamu pod wybranego DPS
- System punktowy oparty o:
  - potrzeby DPS-a,
  - efekty skillów postaci wspierających
- Filtrowanie i wyszukiwanie postaci po:
  - nazwie,
  - roli,
  - elemencie,
  - ścieżce (Path)
- Ochrona stron aplikacji przed dostępem bez zalogowania

## Bezpieczeństwo i walidacja

- Dostęp do stron aplikacji jest możliwy tylko po zalogowaniu
- Endpointy API zawierają walidację danych wejściowych
- Obsługiwane są błędy:
  - braków danych,
  - niepoprawnych relacji,
  - prób dostępu do cudzych zasobów
- Aplikacja zabezpiecza się przed:
  - duplikacją danych,
  - nieprawidłową edycją teamów,
  - błędną konfiguracją drużyn
  
## Środowisko i użyte technologie:
 
 Projekt wykorzystuje lekkie środowisko backendowe oparte na Pythonie oraz popularnych bibliotekach webowych i ORM.
 
 1. **Flask** - minimalistyczny framework do tworzenia API, używany do:
    - obsługi endpointów,
    - uruchamiania serwera,
    - zarządzania kontekstem aplikacji,
    - integracji z SQLAlchemy.
 2. **SQLAlchemy** - ORM (Object-Relational Mapping), który pozwala definiować modele danych w Pythonie zamiast pisania SQL ręcznie, używany do:
    - definiowania modeli (User, Character, Team, itp.),
    - obsługi relacji 1:N oraz N:N,
    - migracji i inicjalizacji bazy.
 3. **SQLite** - lekka, plikowa baza danych, odpowiedzialna za tworzenie pliku .db.
 4. **Wirtualne środowisko (venv)**:
    - umożliwia łatwe odtworzenie środowiska na innym urządzeniu,
    - utrzymuje spójność wersji bibliotek.
 5. **Postman** - klient APi, używany do testowania endpointów API.

## Frontend: 

### Budowa projektu:

<img width="294" height="440" alt="image" src="https://github.com/user-attachments/assets/07784554-c9e6-48b6-8c7f-6674a2d61258" />

 
1. **static** - folder na pliki statyczne:
    - **css** - folder zawierający pliki o formacie .css opowiedzialne za forme prezentacji poszczególnych stron:
       - **characters.css**
       - **style.css** - do main.html
       - **teams.css**
       - **login.css** - do index.html
    - **fonts** - folder zawierający czcionki
    - **img** - zawiera zdjęcia wykorzystane do projektu
    - **scripts** - zawiera pliki o formacie .js
       - **index.js** 
       - **main.js**
       - **characters.js**
       - **teams.js**
2. **templates** - folder składujący pliki o formacie .html
     - **index.html**
     - **mains.html**
     - **characters.html**
     - **teams.html**
     
## Backend:

### Budowa projektu: 
 
<img width="275" height="481" alt="image" src="https://github.com/user-attachments/assets/7723e976-9324-4d64-be25-c8a6ebf50e5f" />

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
    - CRUD dla postaci (w ramach testu),
    - przypisywanie postaci do użytkownika,
    - tworzenie/usuwanie drużyn,
    - listowanie postaci i drużyn użytkownika.
11. **views_html.py** - wartstwa kontaktowa z HTML, zawiera templates dla poszczególnych stron projektu

 
 
