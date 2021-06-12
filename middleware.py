from client import receive_data
import sqlite3
import scholars

class Database():
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect('middleware_db.db')
        self.cursor = self.conn.cursor()
        self.init_database()

    def __del__(self):
        self.conn.close()

    def perform_query(self, query):
        query_results = self.cursor.execute(query)
        return query_results


    def init_database(self):
        # Create table if none exist and add pre existing data 
        try:
            self.perform_query("SELECT * FROM HallOfFame")
            results = self.perform_query("SELECT * FROM HallOfFame")
            # for result in results:
                # print(result)
                # scholar = scholars.Scholar(result)
                # print(scholar)

        except sqlite3.Error:
            self.perform_query('''CREATE TABLE HallOfFame
               (achievement text, name text, field text, picture_url text)''')
            self.perform_query('''INSERT INTO HallOfFame VALUES 
                ("Invented turing machine", "Alan Mathison Turing","Computer science", 
                "https://en.wikipedia.org/wiki/Alan_Turing#/media/File:Alan_Turing_Aged_16.jpg")''')

            self.perform_query('''INSERT INTO HallOfFame VALUES 
                ("God's plan", "Aubrey Drake Graham","Music", 
                "https://en.wikipedia.org/wiki/Drake_(musician)#/media/File:Drake_July_2016.jpg")''')

            self.conn.commit()
                

if __name__ == "__main__":
    # For database testing
    # conn = sqlite3.connect('middleware_db.db')
    # print("Connected to database")
    # cursor = conn.cursor()

    # results = cursor.execute("SELECT * FROM HallOfFame")
    # for result in results:
    #     print(result)
    # conn.close()
    db = Database("middleware_db.db")
    del db
