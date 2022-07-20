"""^   Matches the beginning of a line
$   Matches the end of the line
.   Matches any character
\s  Matches whitespace
\S  Matches any non-whitespace character
*   Repeats a character zero or more times
*?  Repeats a character zero or more times (non-greedy)
+   Repeats a character one or more times
+?  Repeats a character one or more times (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ]  Matches a single character not in the listed set
[a-z0-9]    The set of characters can include a range
(   Indicates where the string extraction is to start
)   Indicates where the string extraction is to end
"""

# Using re.search() Like find()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstip()
    if line.find('From:') >= 0:
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Using re.search() Like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# The Wild-Card Characters
# The dot characther matches any character
# if you add the asterisk characther, the character is "any number of times"

"""^X.*:"""

# Fine-Tunning Your Match
"""^X.*:"""

"""^X-\S+:"""

# Matching and Extracting Data
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[AEIOU]+', x)
print(y)

# Warning: Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# Non-Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:')
print(y)

# Fine-Tuning String Extraction
x = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
y = re.findall('\S+@\S+', x)
print(y)

y = re.findall('^From (\S+@\S+)', x)
print(y)

data = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

# The Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# The Regex Version
import re
data = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
y = re.findall('@([^ ]*)', data)
print(y)

# Even Cooler Regex Version
import re
data = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
y = re.findall('^From .*@([^ ])', data)
print(y)

# Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# Escape Character
import re
x = "We just received $10.00 for cookies."
y = re.findall('\$[0-9.]+', x)
print(y)

# Challenge
import re

handle = open('regex_sum_1447209.txt')
datalist = list()
tot = 0
for coll in handle:
    coll = coll.strip()
    dump = re.findall('[0-9]+', coll)
    c = 0
    for value in dump:
            data = int(dump[c])
            c += 1
            datalist.append(data)
for value in datalist:
    tot = tot + value
print('The total is:', tot)
