from db import SQLite

sql = SQLite('f.sqlite3')

print(sql.read_table())