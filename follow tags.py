import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = 0
namelist = list()
tags = soup('a')
for tag in tags:
    count = count + 1
    if count == 3:
        print(tag.get('href', None))
        name = tag.contents[0]
        namelist.append(name)
        url = tag.get('href', None)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        count = 0
        tags = soup('a')
        for tag in tags:
            count = count + 1
            if count == 3:
                print(tag.get('href', None))
                name = tag.contents[0]
                namelist.append(name)
print(namelist)
