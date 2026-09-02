from bs4 import BeautifulSoup
import requests

# отправляем запрос
url = "https://books.topscrape.com/"
response = requests.get(url)

# получаем HTML-код страницы
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# поиск заголовка страницы
title = soup.title.text
print(f"Заголовок страницы: {title}")

