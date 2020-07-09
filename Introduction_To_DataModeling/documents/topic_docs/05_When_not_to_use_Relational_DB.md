###When Not to Use a Relational Database

* ```Have large amounts of data```: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.
* ```Need to be able to store different data type formats```: Relational databases are not designed to handle unstructured data.
* ```Need high throughput -- fast reads```: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.
* ```Need a flexible schema```: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
* ```Need high availability```: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.
* ```Need horizontal scalability```: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.