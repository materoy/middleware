import sqlite3

conn = sqlite3.connect("mdd.db")

def execute(query):
    conn.execute(query)