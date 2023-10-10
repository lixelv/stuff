import sqlite3
from random import choice, randint
from faker import Faker
from url import from_example_to_email


class SQLite:
    def __init__(self, db_name, f: str = None):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.fake: Faker = Faker(f)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            headquarter INTEGER
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Office (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER,
            address TEXT,
            phone TEXT,
            email TEXT,
            director_name TEXT,
            FOREIGN KEY (company_id) REFERENCES Company(id)
        );
        """)

        self.connect.commit()

    def add_company(self):
        self.cursor.execute("INSERT INTO Company (name) VALUES (?)", (self.fake.name(),))
        company_id = self.cursor.lastrowid
        n = choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, randint(5, 15)])
        for _ in range(n):
            self.cursor.execute("INSERT INTO Office (company_id, address, phone, email, director_name) VALUES (?, ?, ?, ?, ?)",
                            (company_id, self.fake.address(), self.fake.phone_number(), from_example_to_email(self.fake.email()), self.fake.name()))
            self.connect.commit()
        main_office = self.cursor.lastrowid
        self.cursor.execute('UPDATE Company SET headquarter=? WHERE id=?', (main_office, company_id))
        self.connect.commit()

    def get_max_id_company(self):
        self.cursor.execute('SELECT MAX(id) FROM Company')
        result = self.cursor.fetchone()
        max_id = result[0] if result[0] else 0
        return max_id