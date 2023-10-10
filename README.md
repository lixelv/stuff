db.py:
```python
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
```

main.py:
```python
import time
import aiogram, aiogram.types
from parse import capture_full_page_screenshot, driver
from os import environ

token = environ['TELEGRAM']
bot = aiogram.Bot(token)

dp = aiogram.Dispatcher(bot)

@dp.message_handler

```

db.py:
```python
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
```

main.py:
```python
from db import SQLite

times: int = int(input())
sql: SQLite = SQLite('f.sqlite3', 'ru_RU')

for _ in range(times):
    sql.add_company()

```

test.py:
```python
from db import SQLite

sql = SQLite('f.sqlite3')

print(sql.read_table())
```

url.py:
```python
from random import choice


def from_example_to_email(mail):
    return mail.split('@')[0]+'@'+choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'yandex.ru', 'mail.ru', 'bk.ru'])
```

db.py:
```python
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
```

main.py:
```python
import time
import aiogram, aiogram.types
from parse import capture_full_page_screenshot, driver
from os import environ

token = environ['TELEGRAM']
bot = aiogram.Bot(token)

dp = aiogram.Dispatcher(bot)

@dp.message_handler

```

parse.py:
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def capture_full_page_screenshot(driver, url, name=None, width=1920):
    try:
        start_time = time.perf_counter()
        driver.get(url)
        title = driver.title
        name = title if name == None else name
        scroll_height = driver.execute_script('return document.documentElement.scrollHeight')
        driver.set_window_size(width, scroll_height)
        create_folder_if_not_exists("image")
        screenshot = driver.save_screenshot('image/'+name+'.png')
        print(f"Скриншот сохранен в файле '{name}.png'")

    finally:
        end_time = time.perf_counter()
        return (title, end_time - start_time)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=chrome_options)

url = input('Введите ссылку на сайт: ')
while url != '':
    print(capture_full_page_screenshot(driver, url))
    url = input('Введите ссылку на сайт: ')
driver.quit()

```

main.py:
```python
def find_it(seq):
    m = seq[0]
    for i in list(set(seq)):
        print(f'i={i}, m={m}')
        if (seq.count(i) % 2 != 0 and seq.count(m) % 2 == 0) or (seq.count(i) % 2 != 0 and seq.count(i) > seq.count(m)):
            m = i
    return m

if __name__ == '__main__':
    print(find_it([int(i) for i in input().split(',')]))
```

main.py:
```python
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

```

test.py:
```python
print(' ')
```

db.py:
```python
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

```

main.py:
```python
from db import SQLite
from faker import Faker

times: int = int(input())
fake: Faker = Faker('ru_RU')
un: Faker.unique = fake.unique
sql: SQLite = SQLite('f.sqlite3')

for _ in range(times):
    sql.add_user(un.name(), un.email(), un.phone_number(), un.address())

```

test.py:
```python
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["День", "Прием пищи", "Блюдо", "Калории", "Вес"]

table.add_row(["Понедельник", "Завтрак", "Омлет из 2-х яиц с овощами 🥚🥦", "400 ккал", "200 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "", "Апельсин 🍊", "", "150 г"])
table.add_row(["", "Обед", "Салат из свежих овощей 🥗", "500 ккал", "200 г"])
table.add_row(["", "", "Тушеная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Картофельное пюре 🥔", "", "200 г"])
table.add_row(["", "", "Яблоко 🍏", "", "150 г"])
table.add_row(["", "Ужин", "Гречка 🍚", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие огурцы 🥒", "", "200 г"])
table.add_row(["", "", "Банан 🍌", "", "150 г"])
table.add_row(["", "", "", "", ""])
# Вторник
table.add_row(["Вторник", "Завтрак", "Овсянка на воде 🥣", "400 ккал", "200 г"])
table.add_row(["", "", "Ягоды 🍓", "", "150 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "Обед", "Суп из ленса 🍲", "500 ккал", "300 г"])
table.add_row(["", "", "Отварная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Салат из свежих овощей 🥗", "", "200 г"])
table.add_row(["", "", "Груша 🍐", "", "150 г"])
table.add_row(["", "Ужин", "Картофельный салат 🥔", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие помидоры 🍅", "", "200 г"])
table.add_row(["", "", "Киви 🥝", "", "150 г"])
table.add_row(["", "", "", "", ""])
# Среда
table.add_row(["Среда", "Завтрак", "Творог нежирный 🧀", "400 ккал", "200 г"])
table.add_row(["", "", "Ягоды 🍓", "", "150 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "Обед", "Суп на рыбном бульоне 🍲", "500 ккал", "300 г"])
table.add_row(["", "", "Отварная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Салат из свежих овощей 🥗", "", "200 г"])
table.add_row(["", "", "Апельсин 🍊", "", "150 г"])
table.add_row(["", "Ужин", "Картофельное пюре 🥔", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие огурцы 🥒", "", "200 г"])
table.add_row(["", "", "Банан 🍌", "", "150 г"])
table.add_row(["", "", "", "", ""])
# Четверг
table.add_row(["Четверг", "Завтрак", "Омлет из 2-х яиц с овощами 🥚🥦", "400 ккал", "200 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "", "Яблоко 🍏", "", "150 г"])
table.add_row(["", "Обед", "Салат из свежих овощей 🥗", "500 ккал", "200 г"])
table.add_row(["", "", "Тушеная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Гречка 🍚", "", "200 г"])
table.add_row(["", "", "Груша 🍐", "", "150 г"])
table.add_row(["", "Ужин", "Картофельный салат 🥔", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие помидоры 🍅", "", "200 г"])
table.add_row(["", "", "Киви 🥝", "", "150 г"])
table.add_row(["", "", "", "", ""])
# Пятница
table.add_row(["Пятница", "Завтрак", "Овсянка на воде 🥣", "400 ккал", "200 г"])
table.add_row(["", "", "Ягоды 🍓", "", "150 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "Обед", "Суп из ленса 🍲", "500 ккал", "300 г"])
table.add_row(["", "", "Отварная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Салат из свежих овощей 🥗", "", "200 г"])
table.add_row(["", "", "Апельсин 🍊", "", "150 г"])
table.add_row(["", "Ужин", "Картофельное пюре 🥔", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие огурцы 🥒", "", "200 г"])
table.add_row(["", "", "Банан 🍌", "", "150 г"])
table.add_row(["", "", "", "", ""])
# Суббота
table.add_row(["Суббота", "Завтрак", "Творог нежирный 🧀", "400 ккал", "200 г"])
table.add_row(["", "", "Ягоды 🍓", "", "150 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "Обед", "Суп на рыбном бульоне 🍲", "500 ккал", "300 г"])
table.add_row(["", "", "Отварная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Салат из свежих овощей 🥗", "", "200 г"])
table.add_row(["", "", "Яблоко 🍏", "", "150 г"])
table.add_row(["", "Ужин", "Гречка 🍚", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие помидоры 🍅", "", "200 г"])
table.add_row(["", "", "Киви 🥝", "", "150 г"])

# Воскресенье
table.add_row(["Воскресенье", "Завтрак", "Омлет из 2-х яиц с овощами 🥚🥦", "400 ккал", "200 г"])
table.add_row(["", "", "Отрубной хлеб 🍞", "", "30 г"])
table.add_row(["", "", "Груша 🍐", "", "150 г"])
table.add_row(["", "Обед", "Салат из свежих овощей 🥗", "500 ккал", "200 г"])
table.add_row(["", "", "Тушеная рыба 🐟", "", "150 г"])
table.add_row(["", "", "Картофельное пюре 🥔", "", "200 г"])
table.add_row(["", "", "Апельсин 🍊", "", "150 г"])
table.add_row(["", "Ужин", "Картофельный салат 🥔", "600 ккал", "200 г"])
table.add_row(["", "", "Отварная курица 🍗", "", "150 г"])
table.add_row(["", "", "Свежие огурцы 🥒", "", "200 г"])
table.add_row(["", "", "Банан 🍌", "", "150 г"])

print(table)

```

main.py:
```python
import os, zipfile, random

def get_packed(in_dir, output_directory: str):
    files_list = [os.path.join(in_dir, i) for i in os.listdir(in_dir)]
    output = os.path.join(output_directory, os.path.splitext(random.choice(files_list))[0])+'.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in files_list:
            zipf.write(os.path.join(f))


a = input('Введите путь: ')
a = a if a else os.getcwd()
get_packed(a, a)


```