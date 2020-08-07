###WHERE clause
* Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the WHERE clause
* Failure to include a WHERE clause will result in an error

####Additional Resource
* AVOID using "ALLOW FILTERING": Here is a reference [in DataStax](https://www.datastax.com/dev/blog/allow-filtering-explained-2) that explains ALLOW FILTERING and why you should not use it.

####Commonly Asked Questions:
Q) Why do we need to use a WHERE statement since we are not concerned about analytics? Is it only for debugging purposes?

Ans) The ```WHERE``` statement is allowing us to do the fast reads. With Apache Cassandra, we are talking about big data -- think terabytes of data -- so we are making it fast for read purposes. Data is spread across all the nodes. By using the ```WHERE``` statement, we know which node to go to, from which node to get that data and serve it back. For example, imagine we have 10 years of data on 10 nodes or servers. So 1 year's data is on a separate node. By using the ```WHERE year = 1``` statement we know which node to visit fast to pull the data from.