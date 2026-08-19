# test_vulns.py
import sqlite3
import subprocess
import os
import pickle
import hashlib

# 1. SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# 2. Command Injection
def run_command(user_input):
    result = subprocess.run("ls " + user_input, shell=True)
    return result

# 3. Hardcoded Secret
import os
import json
import ast
import hashlib
import secrets
import base64

def load_data(raw_bytes):
    try:
        return json.loads(raw_bytes.decode('utf-8'))
    except Exception:
        return ast.literal_eval(raw_bytes.decode('utf-8'))

def read_file(filename):
    base_dir = "/var/www/uploads/"
    safe_path = os.path.normpath(os.path.join(base_dir, filename))
    if not os.path.abspath(safe_path).startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid file path")
    with open(safe_path, "r") as f:
        return f.read()

def hash_password(password):
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return base64.b64encode(salt + dk).decode('utf-8')
    with open(path, "r") as f:
        return f.read()

# 6. Weak Hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

import sqlite3
import os
import subprocess

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
conn.commit()

def ping_host(host):
    subprocess.run(["ping", "-c", "1", host])
