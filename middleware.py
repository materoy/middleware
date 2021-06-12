import sqlite3

class Database():
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect('middleware_db.db')

    def __del__(self):
        self.conn.close()

    def perform_query(self, query):
        self.conn.excecute(query)