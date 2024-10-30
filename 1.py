import requests
from bs4 import BeautifulSoup

def parse_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all('h1')
        for header in headers:
            print(header.text)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")


url = input("Введите URL для парсинга: ")
parse_website(url)
