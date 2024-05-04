import json

def cadist(data, key, value):
    result = []
    for d in data:
        for k, v in d.items():
            if k == key and v == value:
                result.append(d)
    return result

with open('t.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

links = []

selected_region = cadist(cadist(data["children"], "text", "город Санкт-Петербург")[0]["children"], "selected", True)[0]
num = int(selected_region["text"].replace("Территориальная избирательная комиссия №", ""))

for i in selected_region["children"]:
    links.append('http://www.st-petersburg.vybory.izbirkom.ru/' + i["href"])

