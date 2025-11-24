Projekt SpotFinder to platforma do odkrywania i udostępniania interesujących miejsc. Użytkownicy mogą dodawać nowe lokalizacje z opisami i kategoriami, a także przeglądać miejsca dodane przez innych.

Jak uruchomić projekt

Poniższe instrukcje zakładają, że masz zainstalowany Python i pip na swoim systemie.

cd SpotFinder

Utwórz i aktywuj wirtualne środowisko:
code
Bash
download
content_copy
expand_less
python -m venv venv

Aktywacja środowiska:

Windows (Command Prompt): venv\Scripts\activate

Windows (PowerShell): venv\Scripts\Activate.ps1

macOS/Linux: source venv/bin/activate

Zainstaluj zależności:

code
Bash
download
content_copy
expand_less
pip install Django

(W przyszłości, jeśli będziesz miał plik requirements.txt, użyjesz: pip install -r requirements.txt)

Zastosuj migracje bazy danych:

code
Bash
download
content_copy
expand_less
python manage.py makemigrations
python manage.py migrate

Utwórz superużytkownika (administratora) - opcjonalnie, jeśli go jeszcze nie masz:

code
Bash
download
content_copy
expand_less
python manage.py createsuperuser

Postępuj zgodnie z instrukcjami, aby podać nazwę użytkownika, adres e-mail i hasło.

Uruchom serwer deweloperski:

code
Bash
download
content_copy
expand_less
python manage.py runserver

Otwórz projekt w przeglądarce:
Po uruchomieniu serwera, otwórz przeglądarkę i przejdź do:

Strona główna: http://127.0.0.1:8000/

Panel administracyjny: http://127.0.0.1:8000/admin/
