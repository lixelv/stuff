import sqlite3


class SQl():
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    width INTEGER DEFAULT 1920,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")
        self.connect.commit()

    def change(self, sql, values=()):
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()):
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def new_user(self, user_id, user_name):
        self.change('INSERT INTO user(id, name, width) VALUES (?, ?, ?)', (user_id, user_name))

    def user_is(self, user_id):
        return bool(self.read('SELECT id FROM user WHERE id = ?', (user_id,)))

    def change_width(self, user_id, width):
        self.change('UPDATE user SET width=?, WHERE id = ?', (width, user_id))

    def read_width(self, user_id):
        return self.read('SELECT width FROM user WHERE id = ?', (user_id,))[0][0]