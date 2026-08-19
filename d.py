import sqlite3
import subprocess

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    import subprocess

def get_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def run_command(user_input):
    result = subprocess.run(["ls", user_input], capture_output=True, text=True)
    return result
    return cursor.fetchall()

def run_command(user_input):
    import subprocess

def run_command(user_input):
    result = subprocess.run(["ls", user_input], capture_output=True, text=True)
    return result
    return result
