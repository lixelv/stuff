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
