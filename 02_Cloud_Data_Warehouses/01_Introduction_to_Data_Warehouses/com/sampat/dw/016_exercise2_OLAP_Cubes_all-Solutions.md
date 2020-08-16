# Exercise 02 -  OLAP Cubes - Solution

All the databases table in this demo are based on public database samples and transformations
- `Sakila` is a sample database created my `MySql` [Link](https://dev.mysql.com/doc/sakila/en/sakila-structure.html)
- The postgresql version of it is called `Pagila` [Link](https://github.com/devrimgunduz/pagila)
- The facts and dimension tables design is based on O'Reilly's public dimensional modelling tutorial schema [Link](http://archive.oreilly.com/oreillyschool/courses/dba3/index.html)


```python
!PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila_star
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila_star -f Data/pagila-star.sql
```


```python
%load_ext sql
import sql
```

# STEP1 : Connect to the local database where Pagila is loaded


```python
DB_ENDPOINT = "127.0.0.1"
DB = 'pagila'
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

# STEP2 :  Facts & Dimensions are supposed to be loaded from Demo01

![image](../../../documents/images/pagila-star.png)

# Start by a simple cube


```python
%%time
%%sql
SELECT dimDate.day,dimMovie.rating, dimCustomer.city, sum(sales_amount) as revenue
FROM factSales 
JOIN dimMovie     on (dimMovie.movie_key         = factSales.movie_key)
JOIN dimDate      on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer  on (dimCustomer.customer_key = factSales.customer_key)
group by (dimDate.day, dimMovie.rating, dimCustomer.city)
order by revenue desc
limit  20;
```

## Slicing

- Slicing is the reduction of the dimensionality of a cube by 1 e.g. 3 dimensions to 2,  fixing one of the dimensions to a single value
- In the following example we have a 3-deminensional cube on day, rating, and country
- In the example below `rating` is fixed and to "PG-13" which reduces the dimensionality 


```python
%%time
%%sql
SELECT dimDate.day,dimMovie.rating, dimCustomer.city, sum(sales_amount) as revenue
FROM factSales
JOIN dimMovie     on (dimMovie.movie_key         = factSales.movie_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
WHERE dimMovie.rating = 'PG-13'
GROUP by (dimDate.day, dimCustomer.city, dimMovie.rating)
ORDER by revenue desc
LIMIT  20;
```

## Dicing
 - Creating a subcube, same dimensionality, less values for 2 or more dimensions
 - e.g. PG-13


```python
%%time
%%sql
SELECT dimDate.day,dimMovie.rating, dimCustomer.city, sum(sales_amount) as revenue
FROM factSales
JOIN dimMovie     on (dimMovie.movie_key         = factSales.movie_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
WHERE dimMovie.rating in ('PG-13', 'PG')
AND dimCustomer.city in ('Bellevue', 'Lancaster')
AND dimDate.day in ('1', '15', '30')
GROUP by (dimDate.day, dimCustomer.city, dimMovie.rating)
ORDER by revenue desc
LIMIT  20;
```

## Roll-up
- Stepping up the level of aggregation to a large grouping
- e.g.`city` is summed as `country`


```python
%%time
%%sql
SELECT dimDate.day,dimMovie.rating, dimCustomer.country, sum(sales_amount) as revenue
FROM factSales
JOIN dimMovie     on (dimMovie.movie_key         = factSales.movie_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
GROUP by (dimDate.day,  dimMovie.rating, dimCustomer.country)
ORDER by revenue desc
LIMIT  20;
```

## Drill-down
- Breaking up one of the dimensions to a lower level.
- e.g.`city` is broken up to  `districts`


```python
%%time
%%sql
SELECT dimDate.day,dimMovie.rating, dimCustomer.district, sum(sales_amount) as revenue
FROM factSales
JOIN dimMovie     on (dimMovie.movie_key         = factSales.movie_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
GROUP by (dimDate.day, dimCustomer.district, dimMovie.rating)
ORDER by revenue desc
LIMIT  20;
```

# Grouping Sets
- It happens a lot that for a 3 dimensions, you want to aggregate a fact:
    - by nothing (total)
    - then by the 1st dimension
    - then by the 2nd 
    - then by the 3rd 
    - then by the 1st and 2nd
    - then by the 2nd and 3rd
    - then by the 1st and 3rd
    - then by the 1st and 2nd and 3rd
    
- Since this is very common, and in all cases, we are iterating through all the fact table anyhow, there is a move clever way to do that using the SQL grouping statement "GROUPING SETS" 

## total revenue


```python
%%sql
SELECT sum(sales_amount) as revenue
FROM factSales
```

## revenue by country


```python
%%sql
SELECT dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by  dimStore.country
order by dimStore.country, revenue desc;
```

## revenue by month


```python
%%sql
SELECT dimDate.month,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
GROUP by dimDate.month
order by dimDate.month, revenue desc;
```

## revenue by month & country


```python
%%sql
SELECT dimDate.month,dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by (dimDate.month, dimStore.country)
order by dimDate.month, dimStore.country, revenue desc;
```

## revenue total, by month, by country, by month & country All in one shot
- watch the nones


```python
%%time
%%sql
SELECT dimDate.month,dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate  on (dimDate.date_key  = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by grouping sets ((), dimDate.month,  dimStore.country, (dimDate.month,  dimStore.country));

```

# CUBE 
- Group by CUBE (dim1, dim2, ..) , produces all combinations of different lenghts in one go.
- This view could be materialized in a view and queried which would save lots repetitive aggregations

```SQL
SELECT dimDate.month,dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate  on (dimDate.date_key   = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by cube(dimDate.month,  dimStore.country);
```



```python
%%time
%%sql
SELECT dimDate.month,dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by cube(dimDate.month,  dimStore.country);
```

## revenue total, by month, by country, by month & country All in one shot, NAIVE way


```python
%%time
%%sql
SELECT  NULL as month, NULL as country, sum(sales_amount) as revenue
FROM factSales
    UNION all 
SELECT NULL, dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by  dimStore.country
    UNION all 
SELECT cast(dimDate.month as text) , NULL, sum(sales_amount) as revenue
FROM factSales
JOIN dimDate on (dimDate.date_key = factSales.date_key)
GROUP by dimDate.month
    UNION all
SELECT cast(dimDate.month as text),dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by (dimDate.month, dimStore.country)
```
