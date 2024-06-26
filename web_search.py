# web_search.py

import requests
from bs4 import BeautifulSoup

def search_web(query):
    response = requests.get(f'https://www.google.com/search?q={query}')
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'})
    return result.text if result else 'No results found'