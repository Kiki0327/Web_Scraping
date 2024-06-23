import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(f'Retrieving {url}')
html = urllib.request.urlopen(url, context=ctx).read()
print(f'Retrieved: {len(html)} characters')

stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
print(f'Count: {len(lst)}')

list_num = []
for item in lst:
    # print(f'Count: {item.find('count').text}')
    list_num.append(int(item.find('count').text))
print(f'Sum: {sum(list_num)}')