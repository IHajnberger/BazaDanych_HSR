# BazaDanych_HSR - WIP
## Backend: (informacje dla współpracownika)
 > [!IMPORTANT]
 > Budowa projektu: 
 
<img width="283" height="450" alt="image" src="https://github.com/user-attachments/assets/1e56e764-b511-4702-abc1-b4dbe6ab4a6e" />

1. **models** - folder z tablicami 
    - \_\_init\_\_.py - pusty plik, on jest odpowiedzialny za łączenie tego folderu z całością poza
2. **static** - pierdoły od Web Servera do API, nie tykać, to na przyszłość do Frontendu
3. **templates** - to samo co static
4. **\_\_init\_\_.py** - centrala aplikacji Flask, tworzy tabele, łączy całość z API
5. **config.py** - zbiór ustawień, na razie nie ma co tykać, chilluje bombe
6. **extensions.py** - pod SQLAlchemy, też chilluje bombe
7. **runserver.py** - start serwera
8. **seed.py** - tutaj dzieje się magia tworzenia postaci, czysty rawdogging bazy, raj dla masochistów (ogólnie jednorazowe przypisanie danych które będą nadane z góry)
9. **views.py** - warstwa kontaktowa z aplikacją, używana do testów w uglyahh localhostcie

 > [!IMPORTANT]
 > Dodatkowe informacje:
 
Nie wiem jak to działa w VS Code, ale i tak Ci napisze rzeczy które musiałam dodać żeby działało/ co używałam itp

1. Flask - to jest ogólnie połączone z tych SQLAlchemy, ja to pobierałam jako pip install flask flask_sqlalchemy (z menu "Python Environments");
2. venv (env) - środowisko pythonowe w którym jest to robione, mi to automatycznie VS pobrał otwierając ten projekt przez Flaskowy Web Projekt, ale ty będziesz to musiał sam ogarnąć;
3. Debug - musiałam w Debug Properties projektu dodać Working Directory bo nie było, ale ogólnie żeby Ci generowało plik bazy (.dp w instance) to musi to wyglądać tak:
    - startup file: BD_Backend\runserver.py
    - working directory: BD_Backend
4. On chce mieć jakiś podgląd do tej bazy nie, i on dał jakieś propozycje programów ale ja pobrałam po prostu "DB Broswer for SQLite"
  


 
