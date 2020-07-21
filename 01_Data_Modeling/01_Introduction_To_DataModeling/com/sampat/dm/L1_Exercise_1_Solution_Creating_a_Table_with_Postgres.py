#!/usr/bin/env python
# coding: utf-8

# # Lesson 1 Exercise 1: Creating a Table with PostgreSQL
# 
# <img src="images/postgresSQLlogo.png" width="250" height="250">

# ### Walk through the basics of PostgreSQL. You will need to complete the following tasks:
# <li>Create a table in PostgreSQL,<li>Insert rows of data<li>Run a simple SQL query to validate the information.

# #### Import the library 
# *Note:* An error might popup after this command has executed. If it does read it careful before ignoring. 

# In[ ]:


import psycopg2


# In[ ]:
from IPython import get_ipython

get_ipython().system('echo "alter user student createdb;" | sudo -u postgres psql')


# ### Create a connection to the database

# In[ ]:


try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)


# ### Use the connection to get a cursor that can be used to execute queries.

# In[ ]:


try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)


# ### Set automatic commit to be true so that each action is committed without having to call conn.commit() after each command. 

# In[ ]:


conn.set_session(autocommit=True)


# ### Create a database to do the work in. 

# In[ ]:


try: 
    cur.execute("create database udacity")
except psycopg2.Error as e:
    print(e)


# #### Add the database name in the connect statement. Let's close our connection to the default database, reconnect to the Udacity database, and get a new cursor.

# In[ ]:


try: 
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try: 
    conn = psycopg2.connect("dbname=udacity")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
    
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)


# ### Create a Song Library that contains a list of songs, including the song name, artist name, year, album it was from, and if it was a single. 
# 
# `song title
# artist
# year
# album
# single`
# 

# In[ ]:


try: 
    cur.execute("CREATE TABLE IF NOT EXISTS songs (song_title varchar, artist_name varchar, year int, album_name varchar, single Boolean);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


# ###  Insert the following two rows in the table
# `First Row:  "Across The Universe", "The Beatles", "1970", "False", "Let It Be"`
# 
# `Second Row: "The Beatles", "Think For Yourself", "False", "1965", "Rubber Soul"`

# In[ ]:


try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single)                  VALUES (%s, %s, %s, %s, %s)",                  ("Across The Universe", "The Beatles", 1970, "Let It Be", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single)                   VALUES (%s, %s, %s, %s, %s)",
                  ("Think For Yourself", "The Beatles", 1965, "Rubber Soul", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# ###  Validate your data was inserted into the table. 
# 

# In[ ]:


try: 
    cur.execute("SELECT * FROM songs;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# ### And finally close your cursor and connection. 

# In[ ]:


cur.close()
conn.close()

