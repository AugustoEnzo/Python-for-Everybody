import sqlite3
import re

conn = sqlite3.connect('/home/ozne/Documents/GitHub/Python for Everybody/SQLite/assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
data = open(fname)
for line in data:
    if not line.startswith('From: '): continue
    domain = re.findall('@([^ ]*)', line)
    temp = str(domain[0])
    org = temp.strip()
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    dataa = str(row[0])
    datab = str(row[1])
    print(dataa, datab)
cur.close()
