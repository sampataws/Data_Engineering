###Differences between HDFS and AWS S3
Since Spark does not have its own distributed storage system, it leverages using HDFS or AWS S3, or any other distributed storage. Primarily in this course, we will be using AWS S3, but let’s review the advantages of using HDFS over AWS S3.

Although it would make the most sense to use AWS S3 while using other AWS services, it’s important to note the differences between AWS S3 and HDFS.

* ```AWS S3``` is an ```object storage system``` that stores the data using key value pairs, namely bucket and key, and ```HDFS``` is an ```actual distributed file system``` which guarantees fault tolerance. HDFS achieves fault tolerance by having duplicate factors, which means it will duplicate the same files at 3 different nodes across the cluster by default (it can be configured to different numbers of duplication).

* HDFS has usually been ```installed in on-premise systems```, and traditionally have had engineers on-site to maintain and troubleshoot Hadoop Ecosystem, which ```cost more than having data on cloud```. Due to the ```flexibility of location``` and ```reduced cost of maintenance```, cloud solutions have been more popular. With extensive services you can use within AWS, S3 has been a more popular choice than HDFS.

* Since ```AWS S3 is a binary object store```, it can ```store all kinds of format```, even images and videos. HDFS will strictly require a certain file format - the popular choices are ```avro``` and ```parquet```, which have relatively high compression rate and which makes it useful to store large dataset.