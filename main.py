import requests
from bs4 import BeautifulSoup
import os

url = 'https://es.dragon-ball-official.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find_all("img")
image_links = []

if not os.path.exists('imagenes'):
    os.makedirs('imagenes')

for i, img in enumerate(results):
    link = img.get('src')
    if not link:
        continue
    if not link.startswith('http'):
        link = url + link
    file_extension = link.split('.')[-1].split('?')[0]
    if file_extension not in ['jpg', 'png', 'webp']:
        continue
    response = requests.get(link)
    with open('imagenes/img{}.{}'.format(i, file_extension), 'wb') as file:
        file.write(response.content)