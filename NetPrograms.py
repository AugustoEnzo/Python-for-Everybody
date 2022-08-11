# # ASCII code for characters that are bytes
# print(ord('H'))
#
# print(ord('e'))
#
# print(ord('\n'))
#
# An HTTP Request in Python
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# Using urllib in Python
# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fhand:
#     print(line.decode().strip())

# Like a file...
# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# BeautifulSoup Installation
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# url = "http://www.dr-chuck.com/page1.htm"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))