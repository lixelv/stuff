import pyautogui
import time

start_from = time.strptime(input("Введите начало (пример: 13:00): "), "%H:%M")
shift = int(input("Сдвиг в минутах: ")) * 60
count = int(input("Количество учеников: "))

time.sleep(5)

a = start_from
c = 0

while True:
    if c >= count:
        break
    
    pyautogui.write(time.sstrftime("%H:%M", a))
    pyautogui.press('enter')
    
    a += shift
    c += 1