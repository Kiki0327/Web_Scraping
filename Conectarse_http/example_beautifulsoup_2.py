import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Initial parameters
url = input('Enter URL - ')
position = int(input('Enter Position - ')) - 1
repetitions = int(input('Enter Repetitions - '))

# Bucle
count = 0
while count < repetitions:
    count += 1

    # Read all url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retriever all of the anchor tags
    tags = soup('a')
    url = str(tags[position].get('href'))
    print(url)