import sqlite3
import subprocess

import subprocess

def get_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def run_command(user_input):
    result = subprocess.run(["ls", user_input], capture_output=True, text=True)
    return result
