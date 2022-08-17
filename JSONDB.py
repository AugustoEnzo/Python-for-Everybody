import json
import sqlite3

conn = sqlite3.connect('/home/ozne/Documents/GitHub/Python for Everybody/SQLite/json.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Functions;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    func_id INTEGER NOT NULL
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

CREATE TABLE Functions (
	id INTEGER NOT NULL PRIMARY KEY UNIQUE,
	name TEXT UNIQUE
);
	
INSERT INTO Functions (id, name) VALUES (0, 'Student');
INSERT INTO Functions (id, name) VALUES (1, 'Instructor');
''')

fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

open_data = open(fname).read()
data = json.loads(open_data)
size = len(data)

print(f'Registers number: {len(data)}')
c = 0

for register in data:
    name = register[0]
    title = register[1]
    func_id = register[2]

    cur.execute('''INSERT OR IGNORE INTO User (name, func_id) VALUES ( ?, ? )''', (name, func_id))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    u_id = cur.fetchone()[0]

    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    try:
        v_insert = cur.fetchone()[0]
    except:
        v_insert = None
    if v_insert is None:
        cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    c_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (u_id, c_id, func_id))
    c += 1
    perc = (c / size) * 100
    print("Percent Accomplished: {:.2f} %".format(perc))

    conn.commit()
