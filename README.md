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

## Opis elementów interaktywnych

### 1. Strona logowania

### Stan początkowy
   
<img width="300"  alt="login" src="https://github.com/user-attachments/assets/8f146a11-3792-4540-bcd1-acc6bad08025" />
  
**Przycisk „Login”**  
  - inicjuje proces logowania  
  - po kliknięciu otwiera okno logowania


### Okno logowania

<img width="300" alt="login_window" src="https://github.com/user-attachments/assets/4a746ae5-7b20-42b2-aa1b-c95b8dfd6028" />

**Pole „Username”**  
  - przyjmuje nazwe użytkownika
  
**Pole „Password”**  
  - przyjmuje hasło użytkownika  
  - znaki są maskowane

**Przycisk „Log In”**  
  - wysyła dane logowania  
  - w przypadku poprawnych danych loguje użytkownika  
  - w przypadku błędu wyświetla komunikat 

**Przycisk „Register now”**  
  - przełącza widok na formularz rejestracji

**Przycisk „X” (prawy górny róg)**  
  - zamyka okno logowania


### Okno create account

<img width="300" alt="register_window" src="https://github.com/user-attachments/assets/ab81741e-face-45db-b9df-f4a21a857102" />

**Pole „Username”**  
  - przyjmuje adres e-mail nowego użytkownika  

**Pole „Password”**  
  - przyjmuje hasło do konta  

**Przycisk „Create”**  
  - tworzy nowe konto użytkownika  
  - po poprawnej rejestracji umożliwia logowanie oraz wyświetla komunikat
  
**Przycisk „Login”**  
  - przełącza widok na formularz logowania

**Przycisk „X” (prawy górny róg)**  
  - zamyka okno rejestracji


### 2. Profil użytkownika

### Widok początkowy - profil użytkownika

  <img width="313" height="302" alt="menu_small" src="https://github.com/user-attachments/assets/10cf62bd-8145-4079-b9eb-73311bd0019c" />

**Przycisk „Menu” (prawy górny róg)**  
  - otwiera listę opcji użytkownika 


### Menu użytkownika

  <img width="311" height="309" alt="menu" src="https://github.com/user-attachments/assets/232489d5-7e45-4cc6-8c55-c172148c0ea4" />
  
**Przycisk „Logout”**  
  - wylogowuje użytkownika z aplikacji  

**Przycisk „Characters”**  
  - przenosi do listy postaci   

**Przycisk „Teams”**  
  - przenosi do kreatora drużyn   

**Przycisk „Menu” lub kliknięcie poza menu**  
  - zamyka menu użytkownika


### 3. Postacie

### Widok początkowy – lista postaci

<img width="800"  alt="chars" src="https://github.com/user-attachments/assets/d5ae8d80-5b8c-4c26-afc9-271e98f1557b" />

**Strzałka w lewo (lewy górny róg):**  
  - powraca do profilu użytkownika.  

**Pole wyszukiwania (prawy górny róg)**  
  - pozwala wyszukać postać po nazwie  

**Filtry (centralna część)**  
  - **Combat type** – filtruje postacie po typie walki  
  - **Path** – filtruje postacie po ścieżce 
  - **Role** – filtruje postacie po roli  

**Lista postaci (poniżej filtrów)**  
  - wszystkie postacie są na początku wyszarzone (nieprzypisane)  
  - kliknięcie w postać przypisuje ją do użytkownika i podświetla kolorem
  - najechanie kursorem wyświetla szczegóły postaci 
    

### 4. Tworzenie drużyn

### Widok początkowy - kreator drużyn

 <img width="800"  alt="teams" src="https://github.com/user-attachments/assets/07439b31-0255-4809-8e32-d188bf86a690" />

 **Pole „Nazwa drużyny”**  
  - umożliwia wpisanie nazwy nowej drużyny  
  - jeśli nie wpiszemy nic, nazwa jest generowana automatycznie jako "New Team"  

**Lista rozwijana – wybór DPS**  
  - pozwala wybrać dostępne postacie DPS z konta użytkownika  

**Pola wyboru – Sustain i Support**  
  - pojawiają się dopiero po wybraniu DPS'a  
  - umożliwiają przypisanie odpowiednich postaci do drużyny  

**Przycisk „Ready”**  
  - aktywny dopiero, gdy wszystkie cztery postacie są wybrane  
  - po kliknięciu tworzy drużynę i dodaje ją do sekcji poniżej

**Przycisk „Delete”**  
- usuwa wybraną drużynę  
- otwiera okno potwierdzenia z opcjami `Confirm` i `Cancel`  

**Przycisk „Edit”**  
- wypełnia pola kreatora aktualnymi danymi drużyny  
- umożliwia edycję istniejącej drużyny i zapisanie zmian  

     
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

 
 
