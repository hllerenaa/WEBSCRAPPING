# pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

datos = urllib.request.urlopen('https://www.facebook.com/hector1h').read().decode()  # Lectura de la pagina
soup = BeautifulSoup(datos, 'html.parser')  # Analizara el contenido objetinido anteriormente
filtro = soup.find_all('a',  class_='_2nlw _2nlv')  # Filtrara con exactitud lo que queremos en este caso la etiqueta
# 'a'
# con un nombre de clase en especifico
print(filtro[0].text)  # Esto retornara un nombre
tags = soup('a')  # Esta filtrara todas las etiquetas 'a'
for tags in tags:  # las recorreremos
    print(tags.get)  # Mostraremos su valor
