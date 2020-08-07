##CAP Theorem:
* ```Consistency```: Every read from the database gets the latest (and correct) piece of data or an error

* ```Availability```: Every request is received and a response is given -- without a guarantee that the data is the latest update

* ```Partition Tolerance```: The system continues to work regardless of losing network connectivity between nodes

###Additional Resource:
You can also check out this [Wikipedia page](https://en.wikipedia.org/wiki/CAP_theorem) on the CAP theorem.

###Commonly Asked Questions:
```1.``` Is Eventual Consistency the opposite of what is promised by SQL database per the ACID principle?
   * Much has been written about how Consistency is interpreted in the ACID principle and the CAP theorem. Consistency in the ACID principle refers to the requirement that only transactions that abide by constraints and database rules are written into the database, otherwise the database keeps previous state. In other words, the data should be correct across all rows and tables. However, consistency in the CAP theorem refers to every read from the database getting the latest piece of data or an error.

To learn more, you may find this discussion useful:

* [Discussion about ACID vs. CAP](https://www.voltdb.com/blog/2015/10/22/disambiguating-acid-cap/)

```2.``` Which of these combinations is desirable for a production system - Consistency and Availability, Consistency and Partition Tolerance, or Availability and Partition Tolerance?

* As the CAP Theorem Wikipedia entry says, "The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability." So there is no such thing as Consistency and Availability in a distributed database since it must always tolerate network issues. You can only have Consistency and Partition Tolerance (CP) or Availability and Partition Tolerance (AP). Remember, relational and non-relational databases do different things, and that's why most companies have both types of database systems.

Does Cassandra meet just Availability and Partition Tolerance in the CAP theorem?
According to the CAP theorem, a database can actually only guarantee two out of the three in CAP. So supporting Availability and Partition Tolerance makes sense, since Availability and Partition Tolerance are the biggest requirements.

If Apache Cassandra is not built for consistency, won't the analytics pipeline break?
If I am trying to do analysis, such as determining a trend over time, e.g., how many friends does John have on Twitter, and if you have one less person counted because of "eventual consistency" (the data may not be up-to-date in all locations), that's OK. In theory, that can be an issue but only if you are not constantly updating. If the pipeline pulls data from one node and it has not been updated, then you won't get it. Remember, in Apache Cassandra it is about Eventual Consistency.