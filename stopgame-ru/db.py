import sqlite3

class DB:
    # region main
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.do("""CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        src TEXT NOT NULL
        )""")

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()
    # endregion

    def insert(self, name, date, src):
        self.do("INSERT INTO data (name, date, src) VALUES (?, ?, ?)", (name, date, src))
