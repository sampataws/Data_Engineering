####1. How to reach First Normal Form (1NF):

* Atomic values: each cell contains unique and single values
* Be able to add data without altering tables
* Separate different relations into different tables
* Keep relationships between tables together with foreign keys
####2. Second Normal Form (2NF):
* Have reached 1NF
* All columns in the table must rely on the Primary Key
####3. Third Normal Form (3NF):
* Must be in 2nd Normal Form
* No transitive dependencies
* Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.
####When to use 3NF:
When you want to update data, we want to be able to do in just 1 place. We want to avoid updating the table in the Customers Detail table (in the example in the lecture slide).