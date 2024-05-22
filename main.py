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

for img in results:
    image_links.append(img['src'])
    print(image_links)
