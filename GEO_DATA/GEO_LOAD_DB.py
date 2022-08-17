import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
from random import randint

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('/home/augenz/PycharmProjects/Python-for-Everybody/GEO_DATA/geodata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fp = open('/home/augenz/PycharmProjects/Python-for-Everybody/GEO_DATA/where.data')
count = c = int()
l_data = list()

for line in fp:
    data_l = line.strip()
    l_data.append(data_l)
    c += 1

while True:

    if count == 200:
        print('Insertion limit reached.')
        break
    r_int = randint(0, c-1)
    address_l = l_data[r_int]
    cur.execute("SELECT geodata FROM Locations WHERE address = ?",
                (memoryview(address_l.encode()), ))
    try:
        data = cur.fetchone()[0]
        print("Found in database ", address_l)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address_l
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count += 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''',
                (memoryview(address_l.encode()), memoryview(data.encode())))

    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit...')
        time.sleep(1)
