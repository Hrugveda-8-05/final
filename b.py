import sqlite3
import subprocess

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def run_command(user_input):
    result = subprocess.run("ls " + user_input, shell=True)
    return result


# DevSecOps Agent Fix:
def run_command(user_input):
    result = subprocess.run(["ls", user_input])
    return result