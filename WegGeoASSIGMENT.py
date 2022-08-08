import urllib.request, urllib.parse
import json
import ssl

service_url = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter the location (Press Enter to exit) : ")
    if len(address) < 1: break

    param = dict()
    param['address'] = address
    param['key'] = 42
    url = service_url + urllib.parse.urlencode(param)

    print('Catching data from:', url)
    uh = urllib.request.urlopen(url, context=ctx)
    info = uh.read().decode()
    print('The length of the data is:', len(info))

    try:
        data = json.loads(info)
    except:
        data = None

    if not data or 'status' not in data or data['status'] != 'OK':
        print('Failure to catch the data')
        print(data)
        continue

    # Uncomment to print the data caught
    # print(json.dumps(data, indent=4))

    place_id = data["results"][0]["place_id"]
    print('The place id for this location is: \n', place_id)
