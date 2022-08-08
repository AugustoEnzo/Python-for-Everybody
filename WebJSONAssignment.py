import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_1447214.json'

uh = urllib.request.urlopen(url)

info = uh.read().decode()


data = json.loads(info)
print(data)
print(f'Comments count: {len(data)}')
sum = cn = 0
for k in data:
    if k == "comments":
        for name in data["comments"]:
            n = name["name"]
            cn += 1
            c = name["count"]
            print(f'Summing the count of comments from user: {n}')
            sum += c
        print(f'The total count was {cn}')
        print(f'The total sum was: {sum}')

