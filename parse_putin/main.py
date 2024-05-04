from bs4 import BeautifulSoup
import json
import requests
# import re

def replace_on_dict(text: str, dict: dict) -> str:
    for i, j in dict.items():
        text = text.replace(i, j)
    return text

def parse_json_after(text: str, after: str) -> dict:
    data_value = ''
    i, c, s = 0, 0, 0
    while i < len(script_content):
        if s:
            if script_content[i] == '{' or script_content[i] == '}':
                c += 1 if script_content[i] == '{' else -1
                data_value += script_content[i]
                
            elif c > 0:
                data_value += script_content[i]
                
        if c == 0:
            s = 0

        if script_content[i-len(after):i] == after:
            s = 1
        i += 1
    return json.loads(data_value)

nums = {
    'Y': '0',
    'Й': '1',
    'o': '2',
    'S': '3',
    'N': '4',
    'ф': '5',
    'E': '6',
    'й': '7',
    'n': '8',
    'c': '9'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

# Предположим, что у вас есть переменная html_content, содержащая HTML-код страницы
html_content = requests.get("http://www.st-petersburg.vybory.izbirkom.ru/region/izbirkom?action=show&root=1000075&tvd=27820002162291&vrn=100100339410030&prver=0&pronetvd=null&region=78&sub_region=78&type=226&report_mode=1").text

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Создаем объект BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем тег <script>
script_tag = soup.find('script')

# Получаем содержимое тега <script>
script_content = script_tag.string

# Извлекаем значение переменной data из содержимого тега <script>

# Теперь переменная data_value содержит значение переменной data
d = parse_json_after(script_content, after='tvdTreeJson =')
with open('t.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(d))

# while True:
# a = requests.get('http://www.st-petersburg.vybory.izbirkom.ru/region/izbirkom?action=show&root=1000075&tvd=27820002162292&vrn=100100339410030&prver=0&pronetvd=null&region=78&sub_region=78&type=226&report_mode=null', headers=headers).text
# with open('nm.html', 'w', encoding='utf-8') as f:
#     f.write(str(a))
# a = BeautifulSoup(a, 'html.parser')
# a = a.find('ul', style_='opacity: 1; transition-duration: 0.5s;')
# print(a)


# http://www.st-petersburg.vybory.izbirkom.ru/region/izbirkom?action=show&root=782000082&tvd=4784001513646&vrn=100100339410030&prver=0&pronetvd=null&region=78&sub_region=78&type=226&report_mode=null # 1 # delta tvd - участок delta root - район
# http://www.st-petersburg.vybory.izbirkom.ru/region/izbirkom?action=show&root=782000083&tvd=4784002486288&vrn=100100339410030&prver=0&pronetvd=null&region=78&sub_region=78&type=226&report_mode=null # 158
# http://www.st-petersburg.vybory.izbirkom.ru/region/izbirkom?action=show&root=782000024&tvd=9789005650010&vrn=100100339410030&prver=0&pronetvd=null&region=78&sub_region=78&type=226&report_mode=null # 611