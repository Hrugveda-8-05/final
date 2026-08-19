# test_vulns.py
import sqlite3
import subprocess
import os
import pickle
import hashlib

import os
import subprocess

def get_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def run_command(user_input):
    result = subprocess.run(["ls", user_input], capture_output=True, text=True)
    return result

SECRET_KEY = os.getenv("SECRET_KEY")
AWS_KEY = os.getenv("AWS_KEY")
    return result

# 3. Hardcoded Secret
import json
import os
import hashlib
import base64

def load_data(raw_bytes):
    if isinstance(raw_bytes, bytes):
        text = raw_bytes.decode('utf-8')
    else:
        text = raw_bytes
    return json.loads(text)

def read_file(filename):
    base_dir = "/var/www/uploads/"
    path = base_dir + filename
    with open(path, "r") as f:
        return f.read()

def hash_password(password):
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt + dk).decode()
    with open(path, "r") as f:
        return f.read()

# 6. Weak Hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

import sqlite3
import subprocess
import os

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
conn.commit()
conn.close()

def ping_host(host):
    subprocess.run(["ping", "-c", "1", host], check=True)


# DevSecOps Agent Fix:
import subprocess
import pickle

def run_command(user_input):
    result = subprocess.run(["ls", user_input])
    return result

SECRET_KEY = "hardcoded_super_secret_123"
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"

def load_data(raw_bytes):
    return pickle.loads(raw_bytes)