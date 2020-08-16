# Exercise 02 -  OLAP Cubes - Slicing and Dicing

All the databases table in this demo are based on public database samples and transformations
- `Sakila` is a sample database created by `MySql` [Link](https://dev.mysql.com/doc/sakila/en/sakila-structure.html)
- The postgresql version of it is called `Pagila` [Link](https://github.com/devrimgunduz/pagila)
- The facts and dimension tables design is based on O'Reilly's public dimensional modelling tutorial schema [Link](http://archive.oreilly.com/oreillyschool/courses/dba3/index.html)

Start by creating and connecting to the database by running the cells below.


```python
!PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila_star
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila_star -f Data/pagila-star.sql
```

### Connect to the local database where Pagila is loaded


```python
import sql
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

### Star Schema
![image](../../../documents/images/pagila-star.png)

# Start with a simple cube
TODO: Write a query that calculates the revenue (sales_amount) by day, rating, and city. Remember to join with the appropriate dimension tables to replace the keys with the dimension labels. Sort by revenue in descending order and limit to the first 20 rows. The first few rows of your output should match the table below.


```python
%%time
%%sql

SELECT...
FROM...
```

<div class="p-Widget jp-RenderedHTMLCommon jp-RenderedHTML jp-mod-trusted jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><table>
    <tbody><tr>
        <th>day</th>
        <th>rating</th>
        <th>city</th>
        <th>revenue</th>
    </tr>
    <tr>
        <td>30</td>
        <td>G</td>
        <td>San Bernardino</td>
        <td>24.97</td>
    </tr>
    <tr>
        <td>30</td>
        <td>NC-17</td>
        <td>Apeldoorn</td>
        <td>23.95</td>
    </tr>
    <tr>
        <td>21</td>
        <td>NC-17</td>
        <td>Belm</td>
        <td>22.97</td>
    </tr>
    <tr>
        <td>30</td>
        <td>PG-13</td>
        <td>Zanzibar</td>
        <td>21.97</td>
    </tr>
    <tr>
        <td>28</td>
        <td>R</td>
        <td>Mwanza</td>
        <td>21.97</td>
    </tr>
</tbody></table></div>

## Slicing

Slicing is the reduction of the dimensionality of a cube by 1 e.g. 3 dimensions to 2, fixing one of the dimensions to a single value. In the example above, we have a 3-dimensional cube on day, rating, and country.

TODO: Write a query that reduces the dimensionality of the above example by limiting the results to only include movies with a `rating` of "PG-13". Again, sort by revenue in descending order and limit to the first 20 rows. The first few rows of your output should match the table below. 


```python
%%time
%%sql

SELECT...
FROM...
```

<div class="p-Widget jp-RenderedHTMLCommon jp-RenderedHTML jp-mod-trusted jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><table>
    <tbody><tr>
        <th>day</th>
        <th>rating</th>
        <th>city</th>
        <th>revenue</th>
    </tr>
    <tr>
        <td>30</td>
        <td>PG-13</td>
        <td>Zanzibar</td>
        <td>21.97</td>
    </tr>
    <tr>
        <td>28</td>
        <td>PG-13</td>
        <td>Dhaka</td>
        <td>19.97</td>
    </tr>
    <tr>
        <td>29</td>
        <td>PG-13</td>
        <td>Shimoga</td>
        <td>18.97</td>
    </tr>
    <tr>
        <td>30</td>
        <td>PG-13</td>
        <td>Osmaniye</td>
        <td>18.97</td>
    </tr>
    <tr>
        <td>21</td>
        <td>PG-13</td>
        <td>Asuncin</td>
        <td>18.95</td>
    </tr>
</tbody></table></div>

## Dicing
Dicing is creating a subcube with the same dimensionality but fewer values for  two or more dimensions. 

TODO: Write a query to create a subcube of the initial cube that includes moves with:
* ratings of PG or PG-13
* in the city of Bellevue or Lancaster
* day equal to 1, 15, or 30

The first few rows of your output should match the table below. 


```python
%%time
%%sql

SELECT...
FROM...
```

<div class="p-Widget jp-RenderedHTMLCommon jp-RenderedHTML jp-mod-trusted jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><table>
    <tbody><tr>
        <th>day</th>
        <th>rating</th>
        <th>city</th>
        <th>revenue</th>
    </tr>
    <tr>
        <td>30</td>
        <td>PG</td>
        <td>Lancaster</td>
        <td>12.98</td>
    </tr>
    <tr>
        <td>1</td>
        <td>PG-13</td>
        <td>Lancaster</td>
        <td>5.99</td>
    </tr>
    <tr>
        <td>30</td>
        <td>PG-13</td>
        <td>Bellevue</td>
        <td>3.99</td>
    </tr>
    <tr>
        <td>30</td>
        <td>PG-13</td>
        <td>Lancaster</td>
        <td>2.99</td>
    </tr>
    <tr>
        <td>15</td>
        <td>PG-13</td>
        <td>Bellevue</td>
        <td>1.98</td>
    </tr>
</tbody></table></div>
