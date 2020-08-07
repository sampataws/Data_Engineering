##Clustering Columns:
* The clustering column will sort the data in sorted ```ascending``` order, e.g., alphabetical order.
* More than one clustering column can be added (or none!)
* From there the clustering columns will sort in order of how they were added to the primary key

    ```note:```
* A primary key uniquely identifies a row.
* A composite key is a key formed from multiple columns.
* A partition key is the primary lookup to find a set of rows, i.e. a partition.
* A clustering key is the part of the primary key that isn't the partition key (and defines the ordering within a partition).
####Examples:

* PRIMARY KEY (a): The partition key is a.
* PRIMARY KEY (a, b): The partition key is a, the clustering key is b.
* PRIMARY KEY ((a, b)): The composite partition key is (a, b).
* PRIMARY KEY (a, b, c): The partition key is a, the composite clustering key is (b, c).
* PRIMARY KEY ((a, b), c): The composite partition key is (a, b), the clustering key is c.
* PRIMARY KEY ((a, b), c, d): The composite partition key is (a, b), the composite clustering key is (c, d).
####Commonly Asked Questions:
Q) ```How many clustering columns can we add?```

Ans) You can use as many clustering columns as you would like. You cannot use the clustering columns out of order in the SELECT statement. You may choose to omit using a clustering column in your SELECT statement. That's OK. Just remember to use them in order when you are using the SELECT statement.

####Additional Resources:
* Here is the [DataStax documentation](https://docs.datastax.com/en/cql/3.3/cql/cql_using/useCompoundPrimaryKeyConcept.html) on Composite Partition Keys.
* This [Stackoverflow](https://stackoverflow.com/questions/24949676/difference-between-partition-key-composite-key-and-clustering-key-in-cassandra) page provides a nice description of the difference between Partition Keys and Clustering Keys.