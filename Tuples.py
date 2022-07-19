# Tuples are like lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)

print(max(y))

for iter in y:
    print(iter)

# Tuples are "immutable"
y = 'ABC'
y[2] = 'D'

z = (5, 4, 3)
z[2] = 0

# Things not to do With Tuples
x (3, 2, 1)
x.sort()
x.append(5)
x.reverse()

# A Tale of Two Sequences
l = list()
dir(l)

t = tuple()
dir(t)

# Tuples and Assignment
(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are Comparable
(0, 1, 2) < (5, 1, 2)

(0, 1, 2000000) < (0, 3, 4)

('Jones', 'Sally') < ('Jones', 'Sam')

('Jones', 'Sally') > ('Adams', 'Sam')

# Sorting Lists of Tuples
d = {'a':10, 'b':1, 'c':22}
d.items()
sorted(d.items())

# Using sorted()
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
for k, v in sorted(d.items()):
    print(k, v)

# Sort by Values Instead of Key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# The top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[0:10]:
    print(key, val)

print( sorted( [ (v, k) for k,v in c. items() ] ))