####When to use a NoSQL Database

* ```Need to be able to store different data type formats```: NoSQL was also created to handle different data configurations: structured, semi-structured, and unstructured data. JSON, XML documents can all be handled easily with NoSQL.
* ```Large amounts of data```: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. NoSQL databases were created to be able to be horizontally scalable. The more servers/systems you add to the database the more data that can be hosted with high availability and low latency (fast reads and writes).
* ```Need horizontal scalability```: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data
* ```Need high throughput```: While ACID transactions bring benefits they also slow down the process of reading and writing data. If you need very fast reads and writes using a relational database may not suit your needs.
* ```Need a flexible schema```: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
* ```Need high availability```: Relational databases have a single point of failure. When that database goes down, a failover to a backup system must happen and takes time.