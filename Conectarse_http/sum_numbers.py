import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retriever all of the anchor tags
tags = soup('span')
lineas = []
for tag in tags:
    lineas.append(str(tag))

# Buscando los numeros
numbers = [re.findall('[0-9]+', linea) for linea in lineas]
for i in range(len(numbers)):
    numbers[i] = numbers[i][0]

# Convirtiendo cada string de la lista en int
numbers = [int(x) for x in numbers]

# Imprimiendo resultado
print(f'La suma de los numeros contenidos en el texto es igual a: {sum(numbers)}')