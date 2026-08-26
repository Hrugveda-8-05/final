
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
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login successful"
    return "Login failed"


# Command Injection - CWE-78
@app.route("/ping", methods=["GET"])
def ping():
    host = request.args.get("host")
    
    # Vulnerable: user input directly in shell command
        import subprocess
    import os
    from flask import Flask, request, abort
    
    app = Flask(__name__)
    
    def ping_host(host):
        result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        return result.stdout
    
    @app.route("/file", methods=["GET"])
    def read_file():
        filename = request.args.get("name")
        if not filename:
            abort(400)
        base_dir = "/var/www/files"
        safe_path = os.path.abspath(os.path.join(base_dir, filename))
        if not safe_path.startswith(os.path.abspath(base_dir) + os.sep):
            abort(403)
        try:
            with open(safe_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            abort(404)
    
    if __name__ == "__main__":
        app.run()
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
        from flask import Flask, request, render_template_string
    
    app = Flask(__name__)
    
    @app.route('/search')
    def search():
        query = request.args.get('q', '')
        template = "<h1>Results for: {{ query }}</h1>"
        return render_template_string(template, query=query)
    
    if __name__ == "__main__":
                if __name__ == "__main__":
            app.run()


if __name__ == "__main__":
    app.run(debug=True)
