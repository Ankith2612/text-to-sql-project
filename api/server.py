# api/server.py

from api import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5050)
