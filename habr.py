KEYWORDS = ['отбеливать', 'здоровье']

import requests
from bs4 import BeautifulSoup

ret = requests.get('https://habr.com/ru/all/')
text = ret.text
soup = BeautifulSoup(text, 'html.parser')
post_preview = soup.find_all('article', class_='post post_preview')

for hub in post_preview:
   text = hub.text.strip()
   for vsl in KEYWORDS:
      if vsl in text:
         date = hub.find('span', class_='post__time').text
         print(date.title())
         heading = hub.find('a', class_='post__title_link').text
         print(f'"{heading}"')
         link = hub.find('a', class_='btn btn_x-large btn_outline_blue post__habracut-btn').get('href')
         print(f'---> {link}')
         print("***")





