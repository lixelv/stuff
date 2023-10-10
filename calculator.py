from math import *

while True:
    a = input(">>> ").replace('^', '**')
    if a == '':
        break
    try:
        print(eval(a))
    except Exception as se:
        print(f"Ошибка, {se}")