import requests
from bs4 import BeautifulSoup

def parse_google():
    url = "https://www.google.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

print(parse_google())
