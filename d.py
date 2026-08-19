import sqlite3
import subprocess

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    def fetch_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def run_command(user_input):
    import subprocess
    result = subprocess.run(["ls", user_input])
    return result
    return cursor.fetchall()

def run_command(user_input):
    result = subprocess.run("ls " + user_input, shell=True)
    return result
