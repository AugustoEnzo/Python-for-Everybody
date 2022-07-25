import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/comments_1447211.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum = c = 0
for tag in tags:
    data = tag.decode()
    value = re.findall('<span class="comments">([0-9.]+)', data)
    sum += float(value[0])
    c += 1
print('Count:', c)
print('Sum:', sum)