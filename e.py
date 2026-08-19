from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("users.db")

@app.route("/login")
def login():
    username = request.args.get("username")
    import sqlite3

def login(username, password):
    db = sqlite3.connect('mydb.db')
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
def authenticate(username, password, db):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    user = db.execute(query, (username, password)).fetchone()
    db.close()
    return user
    db.close()
    return user
    )

    user = db.execute(query).fetchone()
    db.close()

    if user:
        return "Login successful"
    return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
