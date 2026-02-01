"""
    Получаем ссылку на сайт которую надо серчить потом извлекаем нужные данные и возвращаем их.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from typing import List, Dict

def search_website(query: str) -> List[Dict[str, str]]:
    base_url = ""
    search_url = f"{base_url}/search?q={quote_plus(query)}"
    response = requests.get(search_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for item in soup.select('.search-result-item'):
        title = item.select_one('.result-title').get_text(strip=True)
        link = item.select_one('a')['href']
        snippet = item.select_one('.result-snippet').get_text(strip=True)
        results.append({
            'title': title,
            'link': link,
            'snippet': snippet
        })
    return results


