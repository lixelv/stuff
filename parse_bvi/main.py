import requests
import re
from collections import Counter
from bs4 import BeautifulSoup


def main():
    result = []

    data = requests.get("https://abit.itmo.ru/order/bachelor/188").text
    soup = BeautifulSoup(data, "html.parser")

    container = soup.select_one(
        "#__next > div > main > div.Background_purple__FnYHm > div > div > div"
    )

    for element in container.find_all("div")[1:]:
        for table_element in element.find_all("tbody"):
            olymp = table_element.find_all("td")[2].text
            result.append(re.sub(r"20\d{2}", "20nn", olymp)[9:])
    with open("result1.json", "w", encoding="utf-8") as file:
        file.write(str(Counter(result)))

    print(sum(Counter(result).values()))


if __name__ == "__main__":
    main()
