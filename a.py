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
    query = "SELECT * FROM users WHERE username = %s"
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


