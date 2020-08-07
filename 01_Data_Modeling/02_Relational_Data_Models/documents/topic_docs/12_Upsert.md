##Upsert
In RDBMS language, the term upsert refers to the idea of inserting a new row in an existing table, or updating the row if it already exists in the table. The action of updating or inserting has been described as "upsert".

The way this is handled in PostgreSQL is by using the ```INSERT``` statement in combination with the ```ON CONFLICT``` clause.

####INSERT
The ```INSERT``` statement adds in new rows within the table. The values associated with specific target columns can be added in any order.

Let's look at a simple example. We will use a customer address table as an example, which is defined with the following ```CREATE``` statement:

```text
CREATE TABLE IF NOT EXISTS customer_address (
    customer_id int PRIMARY KEY, 
    customer_street varchar NOT NULL,
    customer_city text NOT NULL,
    customer_state text NOT NULL
);
```

Let's try to insert data into it by adding a new row:
```text
INSERT into customer_address (
VALUES
    (432, '758 Main Street', 'Chicago', 'IL'
);
```

Now let's assume that the customer moved and we need to update the customer's address. However we do not want to add a new ```customer id```. In other words, if there is any conflict on the customer_id, we do not want that to change.

This would be a good candidate for using the ```ON CONFLICT DO NOTHING``` clause.

```text
INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
VALUES
 (
 432, '923 Knox Street', 'Albany', 'NY'
 ) 
ON CONFLICT (customer_id) 
DO NOTHING;
```

Now, let's imagine we want to add more details in the existing address for an existing customer. This would be a good candidate for using the ```ON CONFLICT DO UPDATE``` clause.

```text
INSERT INTO customer_address (customer_id, customer_street)
VALUES
    (
    432, '923 Knox Street, Suite 1' 
) 
ON CONFLICT (customer_id) 
DO UPDATE
    SET customer_street  = EXCLUDED.customer_street;
```

We recommend checking out these two links to learn other ways to insert data into the tables.

* [PostgreSQL tutorial](http://www.postgresqltutorial.com/postgresql-upsert/)
* [PostgreSQL documentation](https://www.postgresql.org/docs/9.5/sql-insert.html)