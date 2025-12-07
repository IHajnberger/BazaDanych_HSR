import os
from __init__ import create_app
from seed import run_seed

# sciezka do pliku .db
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'database.db')

# usuwamy baze przed utworzeniem aplikacji
if os.path.exists(db_path):
    os.remove(db_path)
    print("Stara baza usunieta")

# teraz tworzysz app
app = create_app()

# dopiero teraz seed w app_context()
with app.app_context():
    run_seed()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
