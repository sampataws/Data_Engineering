###Common Questions:

```What type of companies use Apache Cassandra?```

All kinds of companies. For example, Uber uses Apache Cassandra for their entire backend. Netflix uses Apache Cassandra to serve all their videos to customers. Good use cases for NoSQL (and more specifically Apache Cassandra) are :

* Transaction logging (retail, health care)
* Internet of Things (IoT)
Time series data
* Any workload that is heavy on writes to the database (since Apache Cassandra is optimized for writes).

```Would Apache Cassandra be a hindrance for my analytics work? If yes, why?```
Yes, if you are trying to do analysis, such as using ```GROUP BY``` statements. Since Apache Cassandra requires data modeling based on the query you want, you can't do ad-hoc queries. However you can add clustering columns into your data model and create new tables.