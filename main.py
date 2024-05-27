import requests
from bs4 import BeautifulSoup
import os

url = 'https://es.dragon-ball-official.com/'

try:
    response = requests.get(url)
    response.raise_for_status()  # Verificar si hay errores en la respuesta HTTP
except requests.exceptions.RequestException as e:
    print(f'Error de conexión: {e}')
    exit(1)

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

    try:
        response = requests.get(link)
        response.raise_for_status()  # Verificar si hay errores en la respuesta HTTP
    except requests.exceptions.RequestException as e:
        print(f'Error al descargar la imagen {link}: {e}')
        continue

    try:
        with open(f'imagenes/img{i}.{file_extension}', 'wb') as file:
            file.write(response.content)
    except IOError as e:
        print(f'Error al guardar la imagen {link}: {e}')
        continue