import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/known_by_Pearl.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
c_times = int(input('Insert the times to do it: '))
c_tags = int(input('Insert the position: '))
times = 0
tags = soup('a')
while times != c_times:
    url = url
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    c = 0
    for tag in tags:
        c += 1
        print(f'Position: {c} Retrieving:', tag.get('href', None))
        if c == c_tags:
            url = tag.get('href', None)
            data = str(tag.get('href', None))
            name = re.findall("http://py4e-data.dr-chuck.net/known_by_([a-zA-Z\S]+).html", data)
            break
    times += 1
print("The name that you want's: ", name[0])