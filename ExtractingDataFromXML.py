import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/comments_1447213.xml"
else:
    serviceurl = "http://py4e-data.dr-chuck.net/comments_1447213.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1447213.xml"
if len(url) < 1: quit()
print('Retrieving', url)
r_req = urllib.request.urlopen(url, context=ctx)

data = r_req.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')

sum = 0
for value in comments:
    name = value.find('name').text
    count = value.find('count').text
    sum += int(count)

print(f'The sum is: {sum}')