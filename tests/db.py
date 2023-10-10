import sqlite3
from prettytable import from_db_cursor
from random import randint

class SQLite():
    def __init__(self, db_name, sel_mx_num : int= 100):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL, address TEXT NOT NULL)""")
        self.connect.commit()
        self.select_max_num = sel_mx_num

    def add_user(self, name, email, phone, address):
        self.cursor.execute('INSERT INTO data(name, email, phone, address) VALUES (?,?,?,?)',
                            (name, email, phone, address))
        self.connect.commit()

    def read_table(self):
        self.cursor.execute('SELECT * FROM data WHERE id IN ({})'.format(','.join(['?']*len(self.random_list()))), self.random_list())
        return from_db_cursor(self.cursor)

    def random_list(self):
        max_ = self.cursor.execute('SELECT MAX(id) FROM data').fetchone()[0]
        lst = [randint(1, max_) for _ in range(self.select_max_num)]
        return lst
