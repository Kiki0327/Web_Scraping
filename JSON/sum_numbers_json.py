import urllib.request, urllib.parse, urllib.error
import ssl
import json

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(f'Retrieving {url}')
html = urllib.request.urlopen(url, context=ctx).read()
print(f'Retrieved: {len(html)} characters')

info = json.loads(html)
print(f'Count: {len(info['comments'])}')

list_numbers = []
for item in range(len(info['comments'])):
    list_numbers.append(info['comments'][item]['count'])
print(f'Sum: {sum(list_numbers)}')