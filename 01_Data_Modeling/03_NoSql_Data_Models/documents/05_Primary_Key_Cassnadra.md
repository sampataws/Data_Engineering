###Primary Key
* Must be unique
* The PRIMARY KEY is made up of either just the PARTITION KEY or may also include additional CLUSTERING COLUMNS
* A Simple PRIMARY KEY is just one column that is also the PARTITION KEY. A Composite PRIMARY KEY is made up of more than one column and will assist in creating a unique value and in your retrieval queries
* The PARTITION KEY will determine the distribution of data across the system

Here is the [DataStax documentation](https://docs.datastax.com/en/cql/3.3/cql/cql_using/useSimplePrimaryKeyConcept.html#useSimplePrimaryKeyConcept) on Primary Keys.