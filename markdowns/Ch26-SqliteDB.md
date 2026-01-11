# Sqlite database
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch26-SqliteDB.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- https://www.sqlite.org/
- C-based, one of the most used embedded database (zero configuration)

## SQL basics
- Structured Query Language
- case insensitive language; usually written in uppercase
- let's you or program use SQL-based databases such as SQLite, MySQL, MSSQL, PostgreSQL, etc.
- most important basic statents to learn: CRUD
- C: create (database, table, create and insert records)
- R: retrieve/read data
- U: update data
- D: delete data
- SQL Tutorial and Documentation: http://www.w3schools.com/sql/default.asp
- SQLite and Python Tutorial: https://www.sqlitetutorial.net/sqlite-python/

## sqlite browser
- GUI-based sqlite db explorer
- makes it easy to see data and learn SQL
- http://sqlitebrowser.org/

## sqlite3 module
- python3 provides sqlite3 library to work with sqlite database
- https://docs.python.org/3/library/sqlite3.html
- SQLite natively supports the following types: NULL, INTEGER, REAL, TEXT, BLOB 

|SQLite type|Python type|
| ---|---|
| NULL | None |
| INTEGER | int |
| REAL | float |
| TEXT | str |
| BLOB | bytes |

## in memory db example


```python
import sqlite3
# connect to the memory database
con = sqlite3.connect(":memory:")

# create a table
con.execute("create table person(fname, lname)")
```




    <sqlite3.Cursor at 0x109d803b0>




```python
# fill the table with data
persons = [('Hugo', 'Boss'), ('Calvin', 'Klien')]
con.executemany("insert into person(fname, lname) values (?, ?)", 
                persons)
```




    <sqlite3.Cursor at 0x109d80570>




```python
# print the table contents
for row in con.execute("select rowid, fname, lname from person"):
    print(row)
```

    (1, 'Hugo', 'Boss')
    (2, 'Calvin', 'Klien')



```python
print("I just deleted", con.execute("delete from person where rowid=1").rowcount, 
      "rows")
```

    I just deleted 1 rows


## db file example
### create database, create table and insert data into table


```python
import sqlite3
# create connection
conn = sqlite3.connect('example.db')
# create cursor object
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
                firstName text, 
                lastName text, 
                test1 real, 
                test2 real,
                average real,
                grade text
                )
            """)
```




    <sqlite3.Cursor at 0x109d808f0>




```python
query = """ INSERT INTO students (firstName, lastName, 
            test1, test2) values (?, ?, ?, ?)
        """
cur.execute(query, ('John', 'Smith', 99, 95.5))
```




    <sqlite3.Cursor at 0x109d808f0>




```python
cur.execute(query, ('Michael', 'Jordan', 50, 65))
```




    <sqlite3.Cursor at 0x109d808f0>




```python
# save/commit the changes to the db
conn.commit()
# close the database if done
conn.close()
```

### open database, read and update table


```python
import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()
```


```python
cur.execute('SELECT * FROM students where rowid = 1')
row = cur.fetchone() # returns one row as tuple if rowid with value 1 exists
print(row)
```

    ('John', 'Smith', 99.0, 95.5, None, None)



```python
for col in row:
    print(col)
```

    John
    Smith
    99.0
    95.5
    None
    None



```python
cur.execute('SELECT rowid, * FROM students')
rows = cur.fetchall()
print(type(rows))
```

    <class 'list'>



```python
for row in rows:
    print(row)
```

    (1, 'John', 'Smith', 99.0, 95.5, None, None)
    (2, 'Michael', 'Jordan', 50.0, 65.0, None, None)


<strong>update table</strong>


```python
for row in rows:
    avg = (row[3] + row[4])/2
    # grade = ?
    cur.execute('update students set average=? where rowid=?', (avg, row[0]))
```


```python
cur.execute('select * from students')
print(cur.fetchall())
```

    [('John', 'Smith', 99.0, 95.5, 97.25, None), ('Michael', 'Jordan', 50.0, 65.0, 57.5, None)]



```python
# commit changes and close connection
conn.commit()
conn.close()
```

## SQL Injection Vulnerability
- how not to write sql query in programs


```python
import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
                username text unique, 
                password text 
                )
            """)
```




    <sqlite3.Cursor at 0x109d80730>




```python
# Prompt user to create account
username = input('Enter your username: ')
password = input('Pick a password: ')
```

    Enter your username: john
    Pick a password: password



```python
# bad passwords
# insecure way to create sql statements
sqlinsert = "insert into users (username, password) values ('{0}', '{1}')".format(username, password)
print(sqlinsert)
cur.execute(sqlinsert)

```

    insert into users (username, password) values ('john', 'password')





    <sqlite3.Cursor at 0x109d80730>




```python
# check database
conn.commit()
for row in cur.execute('select * from users'):
    print(row)
```

    ('john', 'password')


### what is wrong with the above codes?

### authenticate users and SQL injection attack


```python
# Prompt user to create account
def insecureAuthentication():
    username = input('Enter your username: ')
    password = input('Pick a password: ')
    sqlSelect = "select * from users where username = '{0}' \
                    and password = '{1}'".format(username, password)
    cur.execute(sqlSelect)
    row = cur.fetchone()
    if row:
        print('Welcome {}, this is your kingdom!'.format(row[0]))
    else:
        print('Wrong credentials. Try Again!')
        
```


```python
insecureAuthentication()
```

    Enter your username: john
    Pick a password: password
    Welcome john, this is your kingdom!



```python
# sql injection; authenticate without using password
insecureAuthentication()
```

    Enter your username: john' or '1'='1
    Pick a password: adfadsfdsf
    Welcome john, this is your kingdom!


## secure way to store password
- https://docs.python.org/3/library/hashlib.html



```python
import uuid
import hashlib, binascii

def createSecurePassword(password, salt=None, round=100000):
    if not salt:
        salt = uuid.uuid4().hex
    
    """
    for i in range(round):
        password = password+salt
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    """
    # hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 
                        salt.encode('utf-8'), round)
    password = binascii.hexlify(dk)
    return "%s:%s"%(password, salt)
```


```python
def secureRegistration():
    # Prompt user to create account
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    secPass = createSecurePassword(password)
    insert = 'insert into users (username, password) values (?, ?)'
    cur.execute(insert, (username, secPass))
    
```


```python
# register a user
secureRegistration()
```

    Enter your username: jake
    Enter your password: password1



```python
# check data
for row in cur.execute('select * from users'):
    print(row)
```

    ('john', 'password')
    ('jake', "b'c318988672d05094deaffce0148a49b1b43dfc89f3b8b75d251de60446dcecc5':5340a4af29574554997b0fe7a1ac670b")



```python
conn.commit()
```


```python
def secureAuthentication():
    username = input('Enter your username: ')
    password = input('Enter your password: ') 
    # use parameterized query
    sqlSelect = 'select password from users where username = ?'
    cur.execute(sqlSelect, (username,))
    row = cur.fetchone()
    if row:
        # username exists
        # check password hashes
        hashpass = row[0]
        hashedPass = hashpass[:hashpass.find(':')]
        salt = hashpass[hashpass.find(':')+1:]
        secPass = createSecurePassword(password, salt)
        if hashpass == secPass:
            print('Welcome to your kingdom, {}'.format(username))
        else:
            print('Wrong credentials. Try Again!')
    else:
        print('Wrong credentials. Try Again!')
```


```python
secureAuthentication()
```

    Enter your username: jake
    Enter your password: password1
    Welcome to your kingdom, jake



```python
# try the same SQL injection
secureAuthentication()
```

    Enter your username: jake' or '1' = '1
    Enter your password: adsfadsf
    Wrong credentials. Try Again!



```python
conn.commit()
conn.close()
```


```python

```
