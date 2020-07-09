###When NOT to use a NoSQL Database?

* ```When you have a small dataset```: NoSQL databases were made for big datasets not small datasets and while it works it wasn’t created for that.
* ```When you need ACID Transactions```: If you need a consistent database with ACID transactions, then most NoSQL databases will not be able to serve this need. NoSQL database are eventually consistent and do not provide ACID transactions. However, there are exceptions to it. Some non-relational databases like MongoDB can support ACID transactions.
* ```When you need the ability to do JOINS across tables```: NoSQL does not allow the ability to do JOINS. This is not allowed as this will result in full table scans.
* ```If you want to be able to do aggregations and analytics```
* ```If you have changing business requirements``` : Ad-hoc queries are possible but difficult as the data model was done to fix particular queries
* ```If your queries are not available and you need the flexibility``` : You need your queries in advance. If those are not available or you will need to be able to have flexibility on how you query your data you might need to stick with a relational database


###Caveats to NoSQL and ACID Transactions
There are some NoSQL databases that offer some form of ACID transaction. As of v4.0, MongoDB added multi-document ACID transactions within a single replica set. With their later version, v4.2, they have added multi-document ACID transactions in a sharded/partitioned deployment.

* Check out this documentation from MongoDB on [multi-document ACID transactions](https://www.mongodb.com/collateral/mongodb-multi-document-acid-transactions)
* Here is another link documenting [MongoDB's ability to handle ACID transactions](https://www.mongodb.com/blog/post/mongodb-multi-document-acid-transactions-general-availability)
Another example of a NoSQL database supporting ACID transactions is MarkLogic.

Check out this link from their [blog](https://www.marklogic.com/blog/how-marklogic-supports-acid-transactions/) that offers ACID transactions.