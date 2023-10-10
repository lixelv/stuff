import requests
from db import DB
from bs4 import BeautifulSoup

sql = DB('db.db')
counter = 1

while True:
    url = f"https://stopgame.ru/review/p{counter}?subsection=izumitelno"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    soup = soup.find("div", class_="_default-grid_1tla4_215").find_all("div")
    for el in soup:
        name = el.find("section", class_="_card__content_givrd_398").find("a").get_text()
        date = el.find("section", class_="_card__date_givrd_1").get_text()
        img = el.find("a", class_="_card__image_givrd_407").find("img").get("src")
        sql.insert(name, date, img)
    counter += 1
    print(counter)
    if len(soup) < 18:
        break
