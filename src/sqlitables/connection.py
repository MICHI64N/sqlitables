import sqlite3

def connect(file_path):
    connection = sqlite3.connect(file_path)
    return connection