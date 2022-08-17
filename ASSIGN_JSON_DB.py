import json
import sqlite3

conn = sqlite3.connect('/home/ozne/Documents/GitHub/Python for Everybody/SQLite/json.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fname = 'roster_data.json'

open_data = open(fname).read()
data = json.loads(open_data)
size = len(data)

print(f'Registers number: {len(data)}')
c = 0

for register in data:
    name = register[0]
    title = register[1]
    func_id = register[2]

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    u_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    c_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES ( ?, ?, ?)''',
                (u_id, c_id, func_id))
    c += 1
    perc = (c / size) * 100
    print('Percent done: {:.2f} %'.format(perc))

    conn.commit()
