import mysql.connector
import prettytable


class DataBase:
    def __init__(self, db_config):
        self.connect = mysql.connector.connect(**db_config)
        self.cursor = self.connect.cursor()

    def read(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def insert_company(self, company_name, ceo, email, phone_number) -> None:
        self.do("INSERT INTO company(name, ceo, email, phone) VALUES (%s, %s, %s, %s);", (company_name, ceo, email, phone_number))

    def insert_office(self, address, ceo, email, phone_number) -> None:
        company_id = self.read("SELECT MAX(id) FROM company")[0][0]
        self.do("INSERT INTO office(company_id, address, ceo, email, phone) VALUES (%s, %s, %s, %s, %s);", (company_id, address, ceo, email, phone_number))

    def update_main_office_id(self):
        max_id = self.read('SELECT MAX(id) FROM company')[0][0]
        self.do("""UPDATE company SET main_office_id = (SELECT MAX(id) FROM office) WHERE id = %s;""", (max_id,))

    def find_company(self, company_name):
        self.cursor.execute("SELECT * FROM company WHERE LOWER(name) LIKE '%' || %s || '%';", (company_name.lower(),))
        result = str(prettytable.from_db_cursor(self.cursor))
        self.cursor.execute("SELECT * FROM office WHERE company_id IN (SELECT id FROM company WHERE LOWER(name) LIKE '%' || %s || '%');", (company_name.lower(),))
        result += '\n'+prettytable.from_db_cursor(self.cursor)

        return result
