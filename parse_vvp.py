# import requests
# from bs4 import BeautifulSoup

# result_dict = {}

# a = requests.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%82%D1%80%D0%B0%D0%BD_%D0%BF%D0%BE_%D0%92%D0%92%D0%9F_(%D0%9F%D0%9F%D0%A1)_%D0%BD%D0%B0_%D0%B4%D1%83%D1%88%D1%83_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F").text
# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(a)
# a = BeautifulSoup(a, 'html.parser')
# a = a.find('table', class_='wikitable sortable ts-columnstyle-increment-1')
# print(a)
# trs = a.find_all('tr')
# for i in trs:
#     if i.find_all('td') != []:
#         if i.find_all('td')[-1].get_text() not in (None, '', ' ', '\n'):
#             result_dict.update({i.find_all('span')[-1].get_text(): int(i.find_all('td')[-1].get_text().replace('\n', ''))})

# print(result_dict)

from matplotlib import pyplot as plt

plt