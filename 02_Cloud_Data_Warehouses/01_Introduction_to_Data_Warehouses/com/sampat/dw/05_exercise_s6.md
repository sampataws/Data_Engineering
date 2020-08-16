# STEP 6: Repeat the computation from the facts & dimension table

Note: You will not have to write any code in this notebook. It's purely to illustrate the performance difference between Star and 3NF schemas.

Start by running the code in the cell below to connect to the database.


```python
!PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila_star
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila_star -f Data/pagila-star.sql
```

     set_config 
    ------------
     
    (1 row)
    
     setval 
    --------
        200
    (1 row)
    
     setval 
    --------
        605
    (1 row)
    
     setval 
    --------
         16
    (1 row)
    
     setval 
    --------
        600
    (1 row)
    
     setval 
    --------
        109
    (1 row)
    
     setval 
    --------
        599
    (1 row)
    
     setval 
    --------
          1
    (1 row)
    
     setval 
    --------
          1
    (1 row)
    
     setval 
    --------
          1
    (1 row)
    
     setval 
    --------
          1
    (1 row)
    
     setval 
    --------
      16049
    (1 row)
    
     setval 
    --------
       1000
    (1 row)
    
     setval 
    --------
       4581
    (1 row)
    
     setval 
    --------
          6
    (1 row)
    
     setval 
    --------
      32098
    (1 row)
    
     setval 
    --------
      16049
    (1 row)
    
     setval 
    --------
          2
    (1 row)
    
     setval 
    --------
          2
    (1 row)
    



```python
%load_ext sql

DB_ENDPOINT = "127.0.0.1"
DB = 'pagila_star'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_PORT = '5432'

# postgresql://username:password@host:port/database
conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

print(conn_string)
%sql $conn_string
```

    postgresql://student:student@127.0.0.1:5432/pagila_star
    (psycopg2.OperationalError) FATAL:  database "pagila_star" does not exist
    
    Connection info needed in SQLAlchemy format, example:
                   postgresql://username:password@hostname/dbname
                   or an existing connection: dict_keys([])


## 6.1 Facts Table has all the needed dimensions, no need for deep joins


```python
%%time
%%sql
SELECT movie_key, date_key, customer_key, sales_amount
FROM factSales 
limit 5;
```

## 6.2 Join fact table with dimensions to replace keys with attributes

As you run each cell, pay attention to the time that is printed. Which schema do you think will run faster?

##### Star Schema


```python
%%time
%%sql
SELECT dimMovie.title, dimDate.month, dimCustomer.city, sum(sales_amount) as revenue
FROM factSales 
JOIN dimMovie    on (dimMovie.movie_key      = factSales.movie_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
group by (dimMovie.title, dimDate.month, dimCustomer.city)
order by dimMovie.title, dimDate.month, dimCustomer.city, revenue desc;
```

##### 3NF Schema


```python
%%time
%%sql
SELECT f.title, EXTRACT(month FROM p.payment_date) as month, ci.city, sum(p.amount) as revenue
FROM payment p
JOIN rental r    ON ( p.rental_id = r.rental_id )
JOIN inventory i ON ( r.inventory_id = i.inventory_id )
JOIN film f ON ( i.film_id = f.film_id)
JOIN customer c  ON ( p.customer_id = c.customer_id )
JOIN address a ON ( c.address_id = a.address_id )
JOIN city ci ON ( a.city_id = ci.city_id )
group by (f.title, month, ci.city)
order by f.title, month, ci.city, revenue desc;
```

# Conclusion

We were able to show that:
* The star schema is easier to understand and write queries against.
* Queries with a star schema are more performant.
