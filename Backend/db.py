import sqlite3

conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
cursor = conn.cursor()
