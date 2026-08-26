
import os
import sqlite3
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials - CWE-798
DATABASE = "users.db"
SECRET_KEY = "hardcoded_secret_key_123"
API_KEY = "sk-prod-abc123xyz456"

def get_db():
    return sqlite3.connect(DATABASE)

# SQL Injection - CWE-89
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    db = get_db()
    cursor = db.cursor()
    
    # Vulnerable: direct string interpolation
        from flask import Flask, request
    import sqlite3
    
    app = Flask(__name__)
    
    def get_db():
        conn = sqlite3.connect('example.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            return "Login successful"
        return "Login failed"
    
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"
    
    if __name__ == '__main__':
        app.run()
        import os
    from flask import Flask, request
    from sqlalchemy import create_engine, text
    
    app = Flask(__name__)
    
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///example.db")
    engine = create_engine(DATABASE_URL)
    
    @app.route("/login", methods=["POST"])
    def login():
        username = request.form["username"]
        password = request.form["password"]
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM users WHERE username=:username AND password=:password"),
                {"username": username, "password": password}
            )
            user = result.fetchone()
        if user:
            return "Login successful"
        return "Login failed"
    
    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"
    user = cursor.fetchone()
    
    if user:
        return "Login successful"
    return "Login failed"


# Command Injection - CWE-78
@app.route("/ping", methods=["GET"])
def ping():
    host = request.args.get("host")
    
    # Vulnerable: user input directly in shell command
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return result.stdout


# Path Traversal - CWE-22
@app.route("/file", methods=["GET"])
def read_file():
    filename = request.args.get("name")
    
    # Vulnerable: no path sanitization
    file_path = os.path.join("/var/www/files", filename)
    with open(file_path, "r") as f:
        return f.read()


# XSS - CWE-79
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    
    # Vulnerable: user input directly in HTML
    template = f"<h1>Results for: {query}</h1>"
    return render_template_string(template)


if __name__ == "__main__":
    app.run(debug=True)
