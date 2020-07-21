# Lesson 1 Demo 0: PostgreSQL and AutoCommits

![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/01_Introduction_To_DataModeling/documents/topic_docs/postgresSQLlogo.png)

## Walk through the basics of PostgreSQL autocommits 


```python
## import postgreSQL adapter for the Python
import psycopg2
```

### Create a connection to the database
1. Connect to the local instance of PostgreSQL (*127.0.0.1*)
2. Use the database/schema from the instance. 
3. The connection reaches out to the database (*studentdb*) and use the correct privilages to connect to the database (*user and password = student*).


```python
conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
```

### Use the connection to get a cursor that will be used to execute queries.


```python
cur = conn.cursor()
```

### Create a database to work in


```python
cur.execute("select * from test")
```

### Error occurs, but it was to be expected because table has not been created as yet. To fix the error, create the table. 


```python
cur.execute("CREATE TABLE test (col1 int, col2 int, col3 int);")
```

### Error indicates we cannot execute this query. Since we have not committed the transaction and had an error in the transaction block, we are blocked until we restart the connection.


```python
conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
cur = conn.cursor()
```

In our exercises instead of worrying about commiting each transaction or getting a strange error when we hit something unexpected, let's set autocommit to true. **This says after each call during the session commit that one action and do not hold open the transaction for any other actions. One action = one transaction.**

In this demo we will use automatic commit so each action is commited without having to call `conn.commit()` after each command. **The ability to rollback and commit transactions are a feature of Relational Databases.**


```python
conn.set_session(autocommit=True)
```


```python
cur.execute("select * from test")
```


```python
cur.execute("CREATE TABLE test (col1 int, col2 int, col3 int);")
```

### Once autocommit is set to true, we execute this code successfully. There were no issues with transaction blocks and we did not need to restart our connection. 


```python
cur.execute("select * from test")
```


```python
cur.execute("select count(*) from test")
print(cur.fetchall())
```


```python

```
