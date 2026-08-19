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
SECRET_KEY = "hardcoded_super_secret_123"
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"


