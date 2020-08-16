# STEP 5: ETL the data from 3NF tables to Facts & Dimension Tables
**IMPORTANT:** The following exercise depends on first having successing completed Exercise 1: Step 4. 

Start by running the code in the cell below to connect to the database. If you are coming back to this exercise, then uncomment and run the first cell to recreate the database. If you recently completed steps 1 through 4, then skip to the second cell.


```python
# !PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila
# !PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-schema.sql
# !PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-data.sql
```


```python
%load_ext sql

DB_ENDPOINT = "127.0.0.1"
DB = 'pagila'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_PORT = '5432'

# postgresql://username:password@host:port/database
conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

print(conn_string)
%sql $conn_string
```

### Introducing SQL to SQL ETL
When writing SQL to SQL ETL, you first create a table then use the INSERT and SELECT statements together to populate the table. Here's a simple example.

First, you create a table called test_table.


```python
%%sql
CREATE TABLE test_table
(
  date timestamp,
  revenue  decimal(5,2)
);
```

Then you use the INSERT and SELECT statements to populate the table. In this case, the SELECT statement extracts data from the `payment` table and INSERTs it INTO the `test_table`.


```python
%%sql
INSERT INTO test_table (date, revenue)
SELECT payment_date AS date,
       amount AS revenue
FROM payment;
```

Then you can use a SELECT statement to take a look at your new table.


```python
%sql SELECT * FROM test_table LIMIT 5;
```

If you need to delete the table and start over, use the DROP TABLE command, like below.


```python
%sql DROP TABLE test_table
```

Great! Now you'll do the same thing below to create the dimension and fact tables for the Star Schema using the data in the 3NF database.

## ETL from 3NF to Star Schema

### 3NF - Entity Relationship Diagram

![image](../../../ipynbFiles/pagila-3nf.png)

### Star Schema - Entity Relationship Diagram

![image](../../../ipynbFiles/pagila-star.png)

In this section, you'll populate the tables in the Star schema. You'll `extract` data from the normalized database, `transform` it, and `load` it into the new tables. 

To serve as an example, below is the query that populates the `dimDate` table with data from the `payment` table.
* NOTE 1: The EXTRACT function extracts date parts from the payment_date variable.
* NOTE 2: If you get an error that says that the `dimDate` table doesn't exist, then go back to Exercise 1: Step 4 and recreate the tables.


```python
%%sql
INSERT INTO dimDate (date_key, date, year, quarter, month, day, week, is_weekend)
SELECT DISTINCT(TO_CHAR(payment_date :: DATE, 'yyyyMMDD')::integer) AS date_key,
       date(payment_date)                                           AS date,
       EXTRACT(year FROM payment_date)                              AS year,
       EXTRACT(quarter FROM payment_date)                           AS quarter,
       EXTRACT(month FROM payment_date)                             AS month,
       EXTRACT(day FROM payment_date)                               AS day,
       EXTRACT(week FROM payment_date)                              AS week,
       CASE WHEN EXTRACT(ISODOW FROM payment_date) IN (6, 7) THEN true ELSE false END AS is_weekend
FROM payment;
```

TODO: Now it's your turn. Populate the `dimCustomer` table with data from the `customer`, `address`, `city`, and `country` tables. Use the starter code as a guide.


```python
%%sql
INSERT INTO dimCustomer (customer_key, customer_id, first_name, last_name, email, address, 
                         address2, district, city, country, postal_code, phone, active, 
                         create_date, start_date, end_date)
SELECT #write code here




       now()         AS start_date,
       now()         AS end_date
FROM customer c
JOIN address a  ON (c.address_id = a.address_id)
JOIN city ci    ON (a.city_id = ci.city_id)
JOIN country co ON (ci.country_id = co.country_id);
```

TODO: Populate the `dimMovie` table with data from the `film` and `language` tables. Use the starter code as a guide.


```python
%%sql
INSERT INTO dimMovie ()
SELECT 
       orig_lang.name AS original_language,
FROM film f
JOIN language l              ON (f.language_id=l.language_id)
LEFT JOIN language orig_lang ON (f.original_language_id = orig_lang.language_id);
```

TODO: Populate the `dimStore` table with data from the `store`, `staff`, `address`, `city`, and `country` tables. This time, there's no guide. You should write the query from scratch. Use the previous queries as a reference.


```python
#Write code here





```

TODO: Populate the `factSales` table with data from the `payment`, `rental`, and `inventory` tables. This time, there's no guide. You should write the query from scratch. Use the previous queries as a reference.


```python
#Write code here





```
