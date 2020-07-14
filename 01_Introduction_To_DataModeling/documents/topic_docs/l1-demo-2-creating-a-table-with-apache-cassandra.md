# Lesson 1 Demo 2: Creating a Table with Apache Cassandra


![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/01_Introduction_To_DataModeling/documents/topic_docs/postgresSQLlogo.png)

## Walk through the basics of Apache Cassandra:<br><li>Creating a table <li>Inserting rows of data<li>Running a simple SQL query to validate the information. 

### Use a python wrapper/ python driver called cassandra to run the Apache Cassandra queries. This library should be preinstalled but in the future to install this library you can run this command in a notebook to install locally: 
`! pip install cassandra-driver`<br>
More documentation can be found here:  https://datastax.github.io/python-driver/

### Import Apache Cassandra python package


```python
import cassandra
```

### Create a connection to the database
1. Connect to the local instance of Apache Cassandra *['127.0.0.1']*.
2. The connection reaches out to the database (*studentdb*) and uses the correct privileges to connect to the database (*user and password = student*).
3. Once we get back the cluster object, we need to connect and that will create our session that we will use to execute queries.<BR><BR>
    
*Note 1:* This block of code will be standard in all notebooks


```python
from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)
 
```

### Test the Connection and Error Handling Code
*Note:* The try-except block should handle the error: We are trying to do a `select *` on a table but the table has not been created yet.


```python
try: 
    session.execute("""select * from music_libary""")
except Exception as e:
    print(e)
 
```

### Create a keyspace to the work in 
*Note:* We will ignore the Replication Strategy and factor information right now as those concepts are covered in depth in Lesson 3. Remember, this will be the strategy and replication factor on a one node local instance. 


```python
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS udacity 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)

except Exception as e:
    print(e)
```

### Connect to our Keyspace.<br>
*Compare this to how a new session in PostgreSQL is created.*


```python
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)
```

### Begin with creating a Music Library of albums. Each album has a lot of information we could add to the music library table. We will  start with album name, artist name, year. 

### But ...Stop

![STOPLOGO](/Users/sampatbudankayala/PycharmProjects/Data_engineering/Introduction_To_DataModeling/documents/topic_docs/stop.jpeg)

### We are working with Apache Cassandra a NoSQL database. We can't model our data and create our table without more information.

### Think about what queries will you be performing on this data?

#### We want to be able to get every album that was released in a particular year. 
`select * from music_library WHERE YEAR=1970`

*To do that:* <ol><li> We need to be able to do a WHERE on YEAR. <li>YEAR will become my partition key,<li>artist name will be my clustering column to make each Primary Key unique. <li>**Remember there are no duplicates in Apache Cassandra.**</ol>

**Table Name:** music_library<br>
**column 1:** Album Name<br>
**column 2:** Artist Name<br>
**column 3:** Year <br>
PRIMARY KEY(year, artist name)


### Now to translate this information into a Create Table Statement. 
More information on Data Types can be found here: https://datastax.github.io/python-driver/<br>
*Note:* Again, we will go in depth with these concepts in Lesson 3.


```python
query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

```

The query should run smoothly.

### Insert two rows 


```python
query = "INSERT INTO music_library (year, artist_name, album_name)"
query = query + " VALUES (%s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Let it Be"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul"))
except Exception as e:
    print(e)
```

### Validate your data was inserted into the table.
*Note:* The for loop is used for printing the results. If executing queries in the cqlsh, this would not be required.

*Note:* Depending on the version of Apache Cassandra you have installed, this might throw an "ALLOW FILTERING" error instead of printing the 2 rows that we just inserted. This is to be expected, as this type of query should not be performed on large datasets, we are only doing this for the sake of the demo.


```python
query = 'SELECT * FROM music_library'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)
```

### Validate the Data Model with the original query.

`select * from music_library WHERE YEAR=1970`


```python
query = "select * from music_library WHERE YEAR=1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)
```

### Drop the table to avoid duplicates and clean up. 


```python
query = "drop table music_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
```

### Close the session and cluster connection


```python
session.shutdown()
cluster.shutdown()
```


```python

```
