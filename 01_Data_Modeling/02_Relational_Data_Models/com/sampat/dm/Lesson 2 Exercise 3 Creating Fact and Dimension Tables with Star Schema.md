
# Lesson 2 Exercise 3: Creating Fact and Dimension Tables with Star Schema

![image](../../../documents/topic_docs/postgresSQLlogo.png)

### Walk through the basics of modeling data using Fact and Dimension tables. You will create both Fact and Dimension tables and show how this is a basic element of the Star Schema. 

#### Where you see ##### you will need to fill in code. 

### This exercise will be more challenging than the last. Use the information provided to create the tables and write the insert statements. 


Note: __Do not__ click the blue Preview button at the bottom

### Import the library 
Note: An error might popup after this command has exectuted. If it does read it careful before ignoring. 


```python
import psycopg2
```

### Create a connection to the database


```python
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
```

### Next use that connect to get a cursor that we will use to execute queries.


```python
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get cursor to the Database")
    print(e)
```

#### For this demo we will use automactic commit so that each action is commited without having to call conn.commit() after each command. The ability to rollback and commit transactions is a feature of Relational Databases. 


```python
conn.set_session(autocommit=True)
```

### Imagine you work at an online Music Store. There will be many tables in our database, but let's just focus on 4 tables around customer purchases. 

![images](../../../ipynbFiles/images/starSchema.png)

### From this representation you can start to see the makings of a "STAR". You will have one fact table (the center of the star) and 3  dimension tables that are coming from it.

### TO-DO: Create the Fact table and insert the data into the table


```python
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
#Insert into all tables 
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

```

### TO-DO: Create the Dimension tables and insert data into those tables.


```python
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
   #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
   #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    #####
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
```

### Now run the following queries on this data easily because of utilizing the Fact/ Dimension and Star Schema
 
#### Query 1: Find all the customers that spent more than 30 dollars, who are they, which store they bought it from, location of the store, what they bought and if they are a rewards member.

#### Query 2: How much did Customer 2 spend?

### Query 1:


```python
try: 
    cur.execute("#####")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
```

### Your output from the above cell should look like this:
('Toby', 1, 'CA', 'Let It Be', False)

### Query 2: 


```python
try: 
    cur.execute("#####")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
```

### Your output from the above cell should include Customer 2 and the amount: 
(2, 35.21)

### Summary: You can see here from this elegant schema that we were: 1) able to get "facts/metrics" from our fact table (how much each store sold), and 2) information about our customers that will allow us to do more indepth analytics to get answers to business questions by utilizing our fact and dimension tables. 

### TO-DO: Drop the tables


```python
try: 
    cur.execute("#####")
    
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
```

### And finally close your cursor and connection. 


```python
cur.close()
conn.close()
```


```python

```
