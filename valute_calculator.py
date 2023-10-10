import requests

data = requests.get('https://www.cbr-xml-daily.ru/latest.js').json()

data = data["rates"]
data.update({'RUB': 1.0})

val_lst = data.keys()
print(val_lst)

cur_from = input('Выберете валюту, из которой вы конвертируете: ').upper()
val_from = float(input('Введите кол-во валюты: '))
cur_to = input('Выберете валюту, в которую конвертируете: ').upper()

result = (data[cur_to]/data[cur_from])*val_from
print(f'{result:.6g} {cur_to}')
