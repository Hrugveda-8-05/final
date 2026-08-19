from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("users.db")

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    db = get_db()

    # VULNERABLE: user input is directly concatenated into SQL
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    user = db.execute(query).fetchone()
    db.close()

    from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=False)
