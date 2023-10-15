from ast import main
import sqlite3

class SQLite():
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        
    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()
        
    def read(self, sql, values=()) -> tuple | list:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()
    