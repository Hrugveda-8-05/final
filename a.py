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
SECRET_KEY = "hardcoded_super_secret_123"
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"

# 4. Insecure Deserialization
def load_data(raw_bytes):
    return pickle.loads(raw_bytes)

# 5. Path Traversal
def read_file(filename):
    base_dir = "/var/www/uploads/"
    path = base_dir + filename
    with open(path, "r") as f:
        return f.read()

# 6. Weak Hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 7. SQL Injection (parameterized missing)
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()

# 8. OS command with user input
def ping_host(host):
    os.system("ping -c 1 " + host)
