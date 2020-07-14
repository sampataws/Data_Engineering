# Lesson 1 Demo 1: Creating a Table with PostgreSQL

![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/01_Introduction_To_DataModeling/documents/topic_docs/postgresSQLlogo.png)

## Walk through the basics of PostgreSQL:<br><li>Creating a table <li>Inserting rows of data, <li>Running a simple SQL query to validate the information. 

### Typically, we would use a python wrapper called *psycopg2* to run the PostgreSQL queries. This library should be preinstalled but in the future to install this library, run the following command in the notebook to install locally: 
!pip3 install --user psycopg2
#### More documentation can be found here: http://initd.org/psycopg/ 

#### Import the library 
Note: An error might popup after this command has executed. Read it carefully before proceeding.


```python
import psycopg2
```

### Create a connection to the database
1. Connect to the local instance of PostgreSQL (*127.0.0.1*)
2. Use the database/schema from the instance. 
3. The connection reaches out to the database (*studentdb*) and uses the correct privileges to connect to the database (*user and password = student*).

### Note 1: This block of code will be standard in all notebooks. 
### Note 2: Adding the try except will make sure errors are caught and understood


```python
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
```

### Use the connection to get a cursor that can be used to execute queries.


```python
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)
```

### Use automactic commit so that each action is commited without having to call conn.commit() after each command. The ability to rollback and commit transactions is a feature of Relational Databases. 


```python
conn.set_session(autocommit=True)
```

### Test the Connection and Error Handling Code
The try-except block should handle the error: We are trying to do a select * on a table but the table has not been created yet.


```python
try: 
    cur.execute("select * from udacity.music_library")
except psycopg2.Error as e:
    print(e)
```

### Create a database to work in 


```python
try: 
    cur.execute("create database udacity")
except psycopg2.Error as e:
    print(e)
```

### Close our connection to the default database, reconnect to the Udacity database, and get a new cursor.


```python
try: 
    conn.close()
except psycopg2.Error as e:
    print(e)
  
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
    
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)
```

### We will create a Music Library of albums. Each album has a lot of information we could add to the music library table. We will  start with album name, artist name, year. 
`Table Name: music_library
column 1: Album Name
column 2: Artist Name
column 3: Year `
### Translate this information into a Create Table Statement. 

Review this document on PostgreSQL datatypes: https://www.postgresql.org/docs/9.5/datatype.html



```python
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS music_library (album_name varchar, artist_name varchar, year int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
```

### No error was found, but lets check to ensure our table was created.  `select count(*)` which should return 0 as no rows have been inserted in the table.


```python
try: 
    cur.execute("select count(*) from music_library")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
print(cur.fetchall())
```

### Insert two rows 


```python
try: 
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                 VALUES (%s, %s, %s)", \
                 ("Let It Be", "The Beatles", 1970))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                 VALUES (%s, %s, %s)", \
                 ("Rubber Soul", "The Beatles", 1965))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
```

### Validate your data was inserted into the table. 
The while loop is used for printing the results. If executing queries in the Postgres shell, this would not be required.

### Note: If you run the insert statement code more than once, you will see duplicates of your data. PostgreSQL allows for duplicates.


```python
try: 
    cur.execute("SELECT * FROM music_library;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
```

### Drop the table to avoid duplicates and clean up


```python
try: 
    cur.execute("DROP table music_library")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
```

###  Close the cursor and connection. 


```python
cur.close()
conn.close()
```
