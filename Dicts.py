purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues']=75
print(purse)
purse['candy'] = purse['candy'] + 2

#####
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen']= ccc['cwen'] + 1
print(ccc)

#####
ccc = dict()
print(ccc['csev'])

#####
counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#####
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

#####
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#####
counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words', words)

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

#####
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for  key in counts:
    print(key, counts[key])

jjj = {'chuck':1, 'fred':42, 'jan':100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#####
for key, value in jjj.items():
    print(key, value)

#####
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)