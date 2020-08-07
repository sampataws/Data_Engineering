###Data Modeling in Apache Cassandra:
* Denormalization is not just okay -- it's a must
* Denormalization must be done for fast reads
* Apache Cassandra has been optimized for fast writes
* ALWAYS think Queries first
* One table per query is a great strategy
* Apache Cassandra does ```not``` allow for JOINs between tables


####Additional Resource:
Here is a reference to the DataStax documents on [Apache Cassandra].(https://docs.datastax.com/en/dse/6.7/cql/cql/ddl/dataModelingApproach.html)