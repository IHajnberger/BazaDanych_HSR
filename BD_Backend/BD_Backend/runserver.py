# start serwera
from __init__ import create_app
from seed import run_seed  # funkcja, która dodaje dane do bazy

app = create_app()

with app.app_context():
    run_seed()  # wype³nia bazê

if __name__ == "__main__":
    app.run(debug=True)
