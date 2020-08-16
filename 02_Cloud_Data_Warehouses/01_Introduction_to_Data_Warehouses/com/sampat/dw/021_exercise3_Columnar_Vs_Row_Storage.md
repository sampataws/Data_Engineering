# Exercise 03 - Columnar Vs Row Storage

- The columnar storage extension used here: 
    - cstore_fdw by citus_data [https://github.com/citusdata/cstore_fdw](https://github.com/citusdata/cstore_fdw)
- The data tables are the ones used by citus_data to show the storage extension



```python
%load_ext sql
```

## STEP 0 : Connect to the local database where Pagila is loaded

### Create the database


```python
!sudo -u postgres psql -c 'CREATE DATABASE reviews;'

!wget http://examples.citusdata.com/customer_reviews_1998.csv.gz
!wget http://examples.citusdata.com/customer_reviews_1999.csv.gz

!gzip -d customer_reviews_1998.csv.gz 
!gzip -d customer_reviews_1999.csv.gz 

!mv customer_reviews_1998.csv /tmp/customer_reviews_1998.csv
!mv customer_reviews_1999.csv /tmp/customer_reviews_1999.csv
```

### Connect to the database


```python
DB_ENDPOINT = "127.0.0.1"
DB = 'reviews'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_PORT = '5432'

# postgresql://username:password@host:port/database
conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

print(conn_string)
```


```python
%sql $conn_string
```

## STEP 1 :  Create a table with a normal  (Row) storage & load data

**TODO:** Create a table called customer_reviews_row with the column names contained in the `customer_reviews_1998.csv` and `customer_reviews_1999.csv` files.


```python
%%sql
DROP TABLE IF EXISTS customer_reviews_row;
CREATE TABLE ...
```

**TODO:** Use the [COPY statement](https://www.postgresql.org/docs/9.2/sql-copy.html) to populate the tables with the data in the `customer_reviews_1998.csv` and `customer_reviews_1999.csv` files. You can access the files in the `/tmp/` folder.


```python
%%sql 
COPY ...
COPY ...
```

## STEP 2 :  Create a table with columnar storage & load data

First, load the extension to use columnar storage in Postgres.


```python
%%sql

-- load extension first time after install
CREATE EXTENSION cstore_fdw;

-- create server object
CREATE SERVER cstore_server FOREIGN DATA WRAPPER cstore_fdw;
```

**TODO:** Create a `FOREIGN TABLE` called `customer_reviews_col` with the column names contained in the `customer_reviews_1998.csv` and `customer_reviews_1999.csv` files.


```python
%%sql
-- create foreign table
DROP FOREIGN TABLE IF EXISTS customer_reviews_col;

-------------
CREATE FOREIGN TABLE #write code here


-------------
-- leave code below as is
SERVER cstore_server
OPTIONS(compression 'pglz');
```

**TODO:** Use the [COPY statement](https://www.postgresql.org/docs/9.2/sql-copy.html) to populate the tables with the data in the `customer_reviews_1998.csv` and `customer_reviews_1999.csv` files. You can access the files in the `/tmp/` folder.


```python
%%sql 
COPY customer_reviews_col FROM '/tmp/customer_reviews_1998.csv' WITH CSV;
COPY customer_reviews_col FROM '/tmp/customer_reviews_1999.csv' WITH CSV;
```

## Step 3: Compare perfromamce

Now run the same query on the two tables and compare the run time. Which form of storage is more performant?

**TODO**: Write a query that calculates the average `review_rating` by `product_title` for all reviews in 1995. Sort the data by `review_rating` in descending order. Limit the results to 20.

First run the query on `customer_reviews_row`:


```python
%%time
%%sql

SELECT...
FROM customer_reviews_row
;
```

 Then on `customer_reviews_col`:


```python
%%time
%%sql

SELECT...
FROM customer_reviews_col
;
```

## Conclusion: We can see that the columnar storage is faster!
