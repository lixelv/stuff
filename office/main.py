from db import SQLite

times: int = int(input())
sql: SQLite = SQLite('f.sqlite3', 'ru_RU')

for _ in range(times):
    sql.add_company()
