main.py:
```py
def cesar(text: str, shift: int, alph: str = 'en') -> str:
    if alph.lower() == 'ru':
        alph: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if alph.lower() == 'en':
        alph: str = 'abcdefghijklmnopqrstuvwxyz'
    alph: str = alph.lower()
    text: list = list(text)
    for i in range(len(text)):
        if text[i] in alph:
            text[i]: str = alph[(alph.index(text[i]) + shift) % len(alph)]
        if text[i] in alph.upper():
            text[i]: str = alph.upper()[(alph.upper().index(text[i]) + shift) % len(alph)]
    return ''.join(text)
with open('text.txt', 'r+', encoding='utf-8') as f:
    text: str = f.read()
    key: int = int(input('Введите ключ: '))
    lang: str = input('Введите язык ru/en: ')
    text: str = cesar(text, key, alph=lang)
    f.seek(0)
    f.write(text)
```
