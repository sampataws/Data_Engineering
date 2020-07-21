#!/usr/bin/env python
# coding: utf-8

# # Lesson 1 Exercise 2: Creating a Table with Apache Cassandra
# <img src="images/cassandralogo.png" width="250" height="250">

# ### Walk through the basics of Apache Cassandra. Complete the following tasks:<li> Create a table in Apache Cassandra, <li> Insert rows of data,<li> Run a simple SQL query to validate the information.

# #### Import Apache Cassandra python package

# In[ ]:



import cassandra

# ### Create a connection to the database

# In[ ]:


from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance.
    session = cluster.connect()
except Exception as e:
    print(e)
 


# ### Create a keyspace to do the work in 

# In[ ]:


try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS udacity 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)

except Exception as e:
    print(e)


# ### Connect to the Keyspace. 

# In[ ]:


try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)


# ### Create a Song Library that contains a list of songs, including the song name, artist name, year, album it was from, and if it was a single. 
# 
# `song title
# artist
# year
# album
# single`

# ### You need to create a table to be able to run the following query: 
# `select * from songs WHERE YEAR=1970 AND artist_name="The Beatles"`

# In[ ]:


query = "CREATE TABLE IF NOT EXISTS songs "
query = query + "(year int, song_title text, artist_name text, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)


# ###  Insert the following two rows in your table
# `First Row:  "Across The Universe", "The Beatles", "1970", "False", "Let It Be"`
# 
# `Second Row: "The Beatles", "Think For Yourself", "False", "1965", "Rubber Soul"`

# In[ ]:


query = "INSERT INTO songs (year, song_title, artist_name, album_name, single)"
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, (1970, "Across The Universe", "The Beatles", "Let It Be", False))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "Think For Yourself", "The Beatles", "Rubber Soul", False))
except Exception as e:
    print(e)


# ###  Validate your data was inserted into the table.

# In[ ]:


query = 'SELECT * FROM songs'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)


# ###  Validate the Data Model with the original query.
# 
# `select * from songs WHERE YEAR=1970 AND artist_name="The Beatles"`

# In[ ]:


query = "select * from songs WHERE YEAR=1970 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)


# ### And Finally close the session and cluster connection

# In[ ]:


session.shutdown()
cluster.shutdown()


# In[ ]:




