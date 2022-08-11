import sqlite3

conn = sqlite3.connect('/home/ozne/Documents/GitHub/Python for Everybody/SQLite/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
data = open(fname)
for line in data:
    if not line.startswith('From: '): continue
    sliced = line.split()
    mail = sliced[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (mail,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''
            INSERT INTO Counts (email, count) VALUES (?, 1)''', (mail, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (mail,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    dataa = str(row[0])
    datab = str(row[1])
    print(dataa, datab)

cur.close()
